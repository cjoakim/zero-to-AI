"""
Generate a dependency graph for a Python library and its transitive dependencies.

Usage:
    python main-networkx.py <library-name>
    python main-networkx.py azure-cosmos
    python main-networkx.py fastapi
    python main-networkx.py jupyter
    python main-networkx.py networkx
    python main-networkx.py openai
    python main-networkx.py zero-to-ai

Reads data/uv/uv-cyclonedx.json (CycloneDX SBOM), builds a directed graph by library
name (versions ignored), extracts the subgraph for the given library and all
transitive dependencies, and writes:
  - networkx/<library>-deps.graphml
  - networkx/<library>-deps.html (pyvis visualization)
"""

import argparse
import json
import sys
from pathlib import Path

from pyvis.network import Network
import networkx as nx

# Chris Joakim, 3Cloud/Cognizant, 2026

DEFAULT_INPUT = "data/uv/uv-cyclonedx.json"
OUTPUT_DIR = "networkx"


def normalize_name(name: str) -> str:
    """Normalize package name for matching (lowercase)."""
    return (name or "").strip().lower()


def load_cyclonedx(path: str) -> dict:
    """Load CycloneDX JSON from path."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_full_graph(data: dict) -> nx.DiGraph:
    """
    Build a directed graph from CycloneDX components and dependencies.
    Nodes are library names (no version). Edge A -> B means A depends on B.
    """
    bom_ref_to_name: dict[str, str] = {}
    for comp in data.get("components", []):
        bom_ref = comp.get("bom-ref") or comp.get("ref")
        name = comp.get("name")
        if bom_ref and name:
            bom_ref_to_name[bom_ref] = name

    graph = nx.DiGraph()
    for comp in data.get("components", []):
        name = comp.get("name")
        if name:
            graph.add_node(name)

    for dep in data.get("dependencies", []):
        ref = dep.get("ref")
        ref_name = bom_ref_to_name.get(ref) if ref else None
        if not ref_name:
            continue
        for dep_ref in dep.get("dependsOn", []):
            dep_name = bom_ref_to_name.get(dep_ref) if dep_ref else None
            if dep_name and dep_name != ref_name:
                graph.add_edge(ref_name, dep_name)

    return graph


def find_library_node(graph: nx.DiGraph, library_arg: str) -> str | None:
    """
    Resolve CLI library argument to a graph node name (exact match after normalize).
    Returns the canonical node name or None if not found.
    """
    target = normalize_name(library_arg)
    for node in graph.nodes():
        if normalize_name(node) == target:
            return node
    return None


def subgraph_transitive_deps(graph: nx.DiGraph, root: str) -> nx.DiGraph:
    """Return subgraph containing root and all nodes reachable from root (transitive deps)."""
    descendants = nx.descendants(graph, root)
    nodes = {root} | descendants
    return graph.subgraph(nodes).copy()


def write_graphml(graph: nx.DiGraph, out_path: str) -> None:
    """Write graph to GraphML file."""
    nx.write_graphml(graph, out_path)


def write_pyvis_html(graph: nx.DiGraph, out_path: str, title: str) -> None:
    """Write interactive HTML visualization using pyvis. Title used in page heading."""
    net = Network(
        directed=True,
        height="800px",
        width="100%",
        bgcolor="#ffffff",
        font_color="#333333",
    )
    title_escaped = title.replace('"', '\\"')
    net.set_options(f"""var options = {{
        "title": "{title_escaped}",
        "edges": {{ "color": {{ "inherit": true }}, "smooth": {{ "enabled": true, "type": "dynamic" }} }},
        "physics": {{ "enabled": true, "stabilization": {{ "enabled": true, "iterations": 1000 }} }}
    }}""")
    for node in graph.nodes():
        net.add_node(node, label=node, title=node, shape="dot", size=10)
    for u, v in graph.edges():
        net.add_edge(u, v, arrows="to")
    net.save_graph(out_path)


def main() -> int:
    """Parse arguments, build graph, and write GraphML + HTML for the given library."""
    parser = argparse.ArgumentParser(
        description="Generate dependency graph for a Python library (with transitive deps)."
    )
    parser.add_argument(
        "library",
        type=str,
        help="Library name (e.g. networkx, fastapi, zero-to-ai)",
    )
    parser.add_argument(
        "-i",
        "--input",
        default=DEFAULT_INPUT,
        help=f"Path to CycloneDX JSON (default: {DEFAULT_INPUT})",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1

    data = load_cyclonedx(str(input_path))
    graph = build_full_graph(data)

    root = find_library_node(graph, args.library)
    if root is None:
        print(
            f"Error: library '{args.library}' not found in the dependency graph.",
            file=sys.stderr,
        )
        print(
            "Libraries are from the project's uv lockfile (uv-cyclonedx.json).",
            file=sys.stderr,
        )
        return 1

    sub = subgraph_transitive_deps(graph, root)
    n_nodes = sub.number_of_nodes()
    n_edges = sub.number_of_edges()
    print(f"Library: {root}")
    print(f"Transitive dependencies: {n_nodes} nodes, {n_edges} edges")

    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    base_name = root.lower().replace("_", "-")
    graphml_path = out_dir / f"{base_name}-deps.graphml"
    html_path = out_dir / f"{base_name}-deps.html"

    write_graphml(sub, str(graphml_path))
    print(f"Wrote {graphml_path}")

    write_pyvis_html(sub, str(html_path), title=f"{root} and transitive dependencies")
    print(f"Wrote {html_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
