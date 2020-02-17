# **craft ai** Python starter kit #

[![Build](https://img.shields.io/travis/craft-ai/craft-ai-starterkit-python/master.svg?style=flat-square)](https://travis-ci.org/craft-ai/craft-ai-starterkit-python) [![License](https://img.shields.io/badge/license-BSD--3--Clause-42358A.svg?style=flat-square)](LICENSE)

[**craft ai** _AI-as-a-service_](http://craft.ai) enables your services to learn every day: provide a personalized experience to each user and automate complex tasks.

This repository hosts a fully working application, in a **Personal Wellness Analysis** context, integrating [**craft ai**](http://craft.ai) written in Python using [**craft ai** official Python client](https://pypi.python.org/pypi?:action=display&name=craft-ai).

The end goal: improve the _sleep_ of the user based on its _historical sleep data_. We have several weeks of data containing _details_ about his day and the time he slept during the night. Using **craft ai**, this simple application learns how well the user sleeps based on his day's data. From this learned model, we can predict how well he may sleep at night and provide meaningful, contextualized advices.

## Tutorial ##

Take a look at the associated [tutorial available on our blog](http://www.craft.ai/blog/)!

## Setup ##

- Download or clone the [sources from GitHub](https://github.com/craft-ai/craft-ai-starterkit-python),
- Install [Python v3.5](https://www.python.org/downloads/) on your computer, alternatively install any version of Python and install [pyenv](https://github.com/pyenv/pyenv#installation),
- Install [pipenv](https://docs.pipenv.org/#install-pipenv-today) to properly manage dependencies,
- Install the dependencies including **craft ai** python client, by running `pipenv install` in the cloned or downloaded repository, from a terminal.
- Create a new project using this [link](https://beta.craft.ai/inspector). You can see that you now have two tokens : the "Read API token" and the "Write API token". Only the latter will be used here. These tokens allow you to authenticate your calls to the **craft ai** API as explained in the [documentation](https://beta.craft.ai/doc/python).
- In the cloned/downloaded repository, create a `.env` file. Fill it with the line `CRAFT_TOKEN=` followed by the Write API token of your project. It should look like this:
    ```
    CRAFT_TOKEN=paste-your-write-token-here
    ```

## Run ##

The following will:

1. create an agent,
2. add a bunch of context operations from the example dataset,
3. compute a decision tree and
4. take a few decisions.

```console
pipenv run start
```

### What to do next ? ###

Now that you know how to compute your decision tree, you are able to complete the initial goal: predict the user's **sleep duration**.

You can add context operations in real time, day after day, and compute a decision when the context changes. It can be used to encourage the user to go to bed at a certain hour in order to have a good night’s sleep.


## About the dataset ##

This starter kit uses real data anonymized and extracted from a personal connected watch owned by a **craft ai** team member. The data is stored in `sleep_data.csv`. Each line corresponds to the day details and the following night sleep. The features are:

* `date` - the date of the day
* `timezone` timezone
* `day_off` - whether or not the user worked this day
* `next_day_off` - whether or not the user work the next day
* `sleep_at_home` - whether or not the user plans to sleep at home
* `sleep_start` - hour at which he started to sleep
* `sleep` - sleep time during the night (hours)

### Data preparation ###

> The pre-treated data are already computed and available for this example.

The data can be treated and then output by the script `src/prepare.py`. The cleaned data is already provided in the `data` folder but you can output it again by running:

```console
pipenv run prepare
```

The result will be set in `data/clean_data.json`.

You can check out `src/prepare.py` to see what we've done and make your own preparation.

> The **craft ai** user documentation can be found at <https://beta.craft.ai/doc> and technical questions can be sent by email at [support@craft.ai]('mailto:support@craft.ai').
