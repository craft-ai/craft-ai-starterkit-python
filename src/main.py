import craftai
import json
import os

## 1) Connect to craftai api
client = craftai.Client({
  "token": os.environ.get("CRAFT_TOKEN")
})

## 2) Create the agent
agent_id = "Wellness"
configuration = {
    "context": {
        "day_off": {                        # day is off or not
            "type": "enum"
        },
        "next_day_off": {                   # next day is off or not
            "type": "enum"
        },
        "sleep_at_home": {                  # sleep at home or not
            "type" : "enum"
        },
        "sleep_start": {                    # hour at which he started to sleep
            "type": "time_of_day",
            "is_generated" : False,
        },
        "timezone": {                       # timezone for sleep_start hour
            "type" : "timezone"
        },
        "sleep": {                          # sleep time during the night
            "type": "continuous"
        }
    },
    "output": ["sleep"],                    # the output is continuous
}

# Delete older version of the agent
client.delete_agent(agent_id)
print("Agent", agent_id, "no longer exists")

# Add the new agent
agent = client.create_agent(configuration, agent_id)
print("Agent", agent["id"], "has successfully been created")

## 3) Load and send the historical data
context_list = []
with open("data/clean_data.json") as data_file:
    context_list = json.load(data_file)

client.add_operations(agent_id, context_list)
print("List of contexts added")

## 4) Retrieve the decison tree
dt_timestamp = 1484521200 # computed tree at the 2017-01-16 (example)
decision_tree = client.get_decision_tree(agent_id, dt_timestamp, 2)

## 5) Compute a decision based on a context
context = {
    "day_off" : "False",             # worked during the day
    "next_day_off" : "True",         # doesn't work the next day
    "sleep_at_home" : "True",        # sleep at home
    "sleep_start" : 23.5,            # start to sleep at 23:30:00
    "timezone" : "+02:00"            # timezone for sleep_start
}
decision = client.decide(decision_tree, context)

print()
print("For the context:", context, "the anticipated sleep time is:", decision["output"]["sleep"]["predicted_value"], "hours")
