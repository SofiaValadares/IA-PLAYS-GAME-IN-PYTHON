levels = [
    {
        "name": "Level 1",
        "grid": [
            [None, None, "green", "blue"],
            [None, None, None, None],
            [None, None, "blue", None],
            ["red", None, None, None]
        ],
        "goal": [
            [None, None, "green", "blue"],
            [None, None, None, None],
            [None, None, "blue", None],
            ["red", None, None, None]
        ],
        "energy_limit": 10  # Define the energy limit for this level
    },
    {
        "name": "Level 2",
        "grid": [
            ["green", None, None, None],
            [None, None, "red", None],
            [None, None, None, None],
            [None, None, None, "blue"]
        ],
        "goal": [
            ["green", None, None, None],
            [None, None, "red", None],
            [None, None, None, None],
            [None, None, None, "blue"]
        ],
        "energy_limit": 15  # Define the energy limit for this level
    },
    {
        "name": "Level 3",
        "grid": [
            [None, "green", None, None],
            [None, None, None, "blue"],
            [None, None, "red", None],
            [None, None, None, None]
        ],
        "goal": [
            [None, "green", None, None],
            [None, None, None, "blue"],
            [None, None, "red", None],
            [None, None, None, None]
        ],
        "energy_limit": 20  # Define the energy limit for this level
    }
]
