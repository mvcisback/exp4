# EXP4 
A python implementation of Exponential weighting for Exploration and Exploitation with Experts. Based on [this blog post](https://banditalgs.com/2016/10/14/exp4/).

This algorithm is useful for non-stochastic Contextual Multi Armed Bandits.

[![Build Status](https://cloud.drone.io/api/badges/mvcisback/exp4/status.svg)](https://cloud.drone.io/mvcisback/exp4)
[![PyPI version](https://badge.fury.io/py/exp4.svg)](https://badge.fury.io/py/exp4)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)

# Installation

If you just need to use `exp4`, you can just run:

`$ pip install exp4`

For developers, note that this project uses the
[poetry](https://poetry.eustace.io/) python package/dependency
management tool. Please familarize yourself with it and then
run:

`$ poetry install`

# Usage

`exp4` is centered around the `exp4.exp4` function which creates a
co-routine for selecting arms given expert advice.

The protocol is as follows:

1. The expert constructs an expert advice matrix.
   - Each row contains the corresponding experts advice vector.
   - The advice vector provides probabilities for each arm.
2. The expert sends a tuple of loss and advice.
   - The loss corresponds to the previous round.
   - The first round's loss is ignored.
   - The advice correspond to the current round.

An example is given below.

```python
from exp4 import exp4

player = exp4()

loss = None           # Will be ignored.
advice = [
    [1/3, 1/3, 1/3],  # Expert 1 
    [2/3, 1/3, 0],    # Expert 2
]
arm = player.send((loss, advice))
assert arm in range(3)

loss = 1 / (1 + arm)  # Arbitrary loss assigned to arm.
advice = [
    [0, 0, 1],        # Expert 1
    [0, 0, 1],        # Expert 2
]
arm = player.send((loss, advice))
assert arm == 2
```
