<h1 align="center">Welcome to Georide-Scripts 👋</h1>
<p>
  <a href="https://github.com/ripoul/Georide-Scripts">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/ripoul/Georide-Scripts/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/ripoulNantes">
    <img alt="Twitter: ripoulNantes" src="https://img.shields.io/twitter/follow/ripoulNantes.svg?style=social" target="_blank" />
  </a>
</p>

> get all your trips (gpx) and some other information about your georide account

### 🏠 [Homepage](https://github.com/ripoul/Georide-Scripts)

## Install

```sh
pip install -r requirements.txt
```

## Usage

To get your georide info for now you can go on https://georide.ripoul.fr/getInfo.

- With a token : 
```sh
python get-trips.py [your tracker id] [ YYYY/MM/DD startDate] [YYYY/MM/DD endDate] -t [your georide token]
```

- With user/password :
```sh
python get-trips.py [your tracker id] [ YYYY/MM/DD startDate] [YYYY/MM/DD endDate] -u [username georide] -p [password georide]
```

## Author

👤 **Jules LE BRIS**

* Twitter: [@ripoulNantes](https://twitter.com/ripoulNantes)
* Github: [@ripoul](https://github.com/ripoul)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/ripoul/Georide-Scripts/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Jules LE BRIS](https://github.com/ripoul).<br />
This project is [MIT](https://github.com/ripoul/Georide-Scripts/blob/master/LICENSE) licensed.
