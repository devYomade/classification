# Number Classification API

The Number Classification API is a RESTful service built with Python and Flask that takes a number as input and returns various mathematical properties about it, along with a fun fact fetched from the Numbers API.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [API Usage](#api-usage)
- [Deployment on AWS EC2](#deployment-on-aws-ec2)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This API evaluates a number and returns the following information:

- **Prime Check:** Determines whether the number is prime.
- **Perfect Number Check:** Determines whether the number is perfect.
- **Armstrong Number Check:** Checks if the number is an Armstrong number.
- **Parity:** Indicates if the number is odd or even.
- **Digit Sum:** Computes the sum of the digits of the number.
- **Fun Fact:** Retrieves a fun mathematical fact from the Numbers API.

## Features

- **Prime Detection:** Determines if the number is prime.
- **Perfect Number Detection:** Checks if the number equals the sum of its proper divisors.
- **Armstrong Number Detection:** Evaluates if the number is equal to the sum of its digits each raised to the power of the number of digits.
- **Parity Evaluation:** Indicates if the number is odd or even.
- **Digit Sum Calculation:** Computes the sum of all the digits in the number.
- **Fun Fact Retrieval:** Uses the Numbers API to fetch an interesting math-related fact.
- **CORS Support:** Configured to handle cross-origin requests.

## Technology Stack

- **Language:** Python 3
- **Framework:** Flask
- **HTTP Library:** Requests
- **CORS:** Flask-CORS

## Installation

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/devYomade/classification.git
cd classification
