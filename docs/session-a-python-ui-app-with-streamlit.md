# Part 1, Session 4 - A Python UI app with Streamlit

The purpose of this session is just to introduce you to Streamlit,
and to show you "the art of the possible" regarding creating Data & AI Web UI applications.

Some of you are more **visual**, and Streamlit UIs may appeal to you more than CLI programs.

We won't, however, be using Steamlit in the remaining sessions of this series.

We'll also cover **PyPI**, the Python Package Index, in this session.

<br><br><br>

## Streamlit

- **Streamlit is a python library to easily create Data & AI Web UI applications**
- **It became popular in recent years for LLM Chat and other AI applications**
- It's great for demonstrations, sample programs, POCs
- You'll encounter Streamlit in your AI Journey - books, blogs, presentations, etc

<br><br><br>

## Demonstration - Example Streamlit application

This session uses file **main-streamlit.py** as our Python CLI program.

### What does this app do?

- Contains a page that generates a graph of similated stock prices
- Contains a page with a simulated LLM chat
- Contains a running calculator that uses my **m26** library

### What does Streamlit do?

- It generates the HTML and CSS for the UI, and the JavaScript for the interactivity
  - From your simple python code 
- Streamlit starts a local web server to host the UI
- Streamlit opens your default web browser to the local web server
- Streamlit also uses websockets to communicate with the browser

### Example of how simple your python code can be

Just six lines of code to generate a simulated stock price chart.

```
with tab1:
    st.header("Stock Price Chart")
    num_months = st.slider('Number of Months', min_value=10, max_value=100)
    if st.button('Line Chart'):
        st.session_state["stock_prices"] = [random.randint(450, 600) for _ in range(num_months)]
        st.line_chart(data=st.session_state["stock_prices"])
```

<p align="center">
   <img src="img/streamlit-simulated-stock-price-chart.png" width="60%">
</p>

### Run the app 

```
streamlit run main-streamlit.py
```

This startup command is different from our previous session, since streamlit
is **both** a library and a command line tool in our python virtual environment.

Previous session - starting a python program from the command line:

```
python main-cli-sample.py add_numbers 1 2 3 4 5
```

### Other Screen Shots from main-streamlit.py

<p align="center">
   <img src="img/streamlit-simulated-chatbot.png" width="60%">
</p>

<p align="center">
   <img src="img/streamlit-m26-calculator.png" width="60%">
</p>

<br><br><br>

## Advanced Streamlit Demos

These are in the Streamlit Gallery, not in this GitHub repository.

- [Streamlit AI Assistant Demo](https://demo-ai-assistant.streamlit.app/?ref=streamlit-io-gallery-favorites)
- [Streamlit Seattle Weather Demo](https://demo-seattle-weather.streamlit.app/?ref=streamlit-io-gallery-favorites)

<p align="center">
   <img src="img/streamlit-seattle-weather-demo.png" width="90%">
</p>

<br><br><br>

## Pro Tip - Get familiar with PyPI, and choose your dependencies wisely

- [PyPI](https://pypi.org)
- [m26 @ PyPI](https://pypi.org/project/m26/)
- [azure-storage-blob @ PyPI](https://pypi.org/project/azure-storage-blob/)

<p align="center">
   <img src="img/pypi-m26.png" width="60%">
</p>

- See the **Maintainers** list.  Prefer libs created by several developers or an organization
- See the **Release History**.  Avoid old libs not recently maintained
- Visit the (GitHub) **Repository**.
  - Look at the source code.  Is it understandable?
  - Look for usable documentation

<br><br><br>

## References

- [Streamlit home page](https://streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Faker @ PyPI](https://pypi.org/project/Faker/) to create simulated/synthetic data
- [m26 @ PyPI](https://pypi.org/project/m26/) running, swimming, and cycling calculations
