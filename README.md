# fundy
library to build techincal indicator-based equities trading strategies. 

[![Build Status](https://github.com/sebastianhereu/fundy/actions/workflows/build.yml/badge.svg)](https://github.com/sebastianhereu/fundy/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/sebastianhereu/fundy/branch/main/graph/badge.svg)](https://codecov.io/gh/sebastianhereu/fundy)
<img src=https://img.shields.io/badge/license-MIT-brightgreen>
<img src=https://img.shields.io/github/issues/sebastianhereu/fundy>

# overview
fundy allows users to compute technical analysis indicators on time series data through a simple API. fundy can also be used to create combination indicators, allowing for the creation of fundamental analysis strategies natively. Strategies can be ran on a basket of stocks and trades can be sent automatically via the Alpaca API

# Usage
Note that use of this library requires the alpaca api. An account may be set up at https://alpaca.markets/. Once you set an account up, you can generate a secret key and an ID key. Paste this information in the fundy/api_config.py, and you're good to go.

