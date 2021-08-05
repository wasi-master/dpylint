<!-- markdownlint-disable-file MD033-->

<!-- PROJECT LOGO -->
<br/>
<p align="center">
  <a href="https://github.com/wasi-master/dpylint">
    <img src="https://raw.githubusercontent.com/wasi-master/dpylint/main/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h2 align="center">dpylint</h2>

  <p align="center">
    An pylint extension for linting discord.py
    <br />
    <a href="https://wasi-master.github.io/dpylint/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/wasi-master/dpylint">View Demo</a>
    ·
    <a href="https://github.com/wasi-master/dpylint/issues">Report Bug</a>
    ·
    <a href="https://github.com/wasi-master/dpylint/issues">Request Feature</a>
  </p>
</p>

<p align="center">
   <a href="https://github.com/wasi-master/dpylint/graphs/contributors"><img src="https://img.shields.io/github/contributors/wasi-master/dpylint.svg?style=flat" alt="Contributors"></a>
   <a href="https://github.com/wasi-master/dpylint/network/members"><img src="https://img.shields.io/github/forks/wasi-master/dpylint.svg?style=flat" alt="Forks"></a>
   <a href="https://github.com/wasi-master/dpylint/stargazers"><img src="https://img.shields.io/github/stars/wasi-master/dpylint.svg?style=flat" alt="Stargazers"></a>
   <a href="https://github.com/wasi-master/dpylint/issues"><img src="https://img.shields.io/github/issues/wasi-master/dpylint.svg?style=flat" alt="Issues"></a>
   <a href="https://github.com/wasi-master/dpylint"><img src="https://img.shields.io/github/languages/code-size/wasi-master/dpylint.svg?style=flat" alt="Code Size"></a>
   <a href="https://github.com/wasi-master/dpylint/blob/master/LICENSE.txt"><img src="https://img.shields.io/github/license/wasi-master/dpylint.svg?style=flat" alt="MIT License"></a>
   <a href="https://saythanks.io/to/arianmollik323@gmail.com"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanke"></a>
   <a href="https://pypistats.org/packages/dpylint"><img src="https://img.shields.io/pypi/dm/dpylint.svg?style=flat" alt="Downloads"></a>
   <a href="https://pypi.org/project/dpylint/#history"><img src="https://img.shields.io/pypi/v/dpylint.svg" alt="Version"></a>
   <a href="https://github.com/wasi-master/dpylint/actions/workflows/python-app.yml"><img src="https://img.shields.io/github/workflow/status/wasi-master/dpylint/Python%20application.svg?label=tests" alt="Tests"></a>
   <a href="https://github.com/wasi-master/dpylint/actions/workflows/python-publish.yml"><img src="https://img.shields.io/github/workflow/status/wasi-master/dpylint/Upload%20Python%20Package.svg?label=build" alt="Build"></a>
   <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![dpylint banner](https://raw.githubusercontent.com/wasi-master/dpylint/main/images/banner.png)](https://wasi-master.github.io/dpylint/)
dpylint is a pylint extension that lints python code written for a discord bot

### Built With

* [python](https://www.python.org)
* [pylint](https://www.pylint.org)

<!-- GETTING STARTED -->
## Getting Started

To install dpylint:

### Prerequisites

You'll need to have [python](https://www.python.org) and [pylint](https://www.pylint.org) installed in order to use the extension

### Installation

* Installing via pip
  1. Directly installing via pip (Recommended)

     ```sh
     pip install dpylint
     ```

  2. Installing using pip and git

     ```sh
     pip install git+https://github.com/wasi-master/dpylint.git
     ```

* Cloning then installing
  1. Clone the repo

     ```sh
     git clone https://github.com/wasi-master/dpylint.git
     ```

  2. Install using pip

     ```sh
     pip install .
     ```

<!-- USAGE EXAMPLES -->
## Usage

Create a new file called `.pylintrc` and add this to that file

```ini
[MASTER]

load-plugins=dpylint
```

_For more examples such as vscode installation, usage without pylintrc file, please refer to the [Documentation](https://wasi-master.github.io/dpylint/)_

<!-- ROADMAP -->
## Roadmap

See the [todo list](https://github.com/wasi-master/dpylint/blob/main/TODO_LIST.md) for a list of features yet to be added(and known issues).
Also see the [open issues](https://github.com/wasi-master/dpylint/issues) issues.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](license.md) for more information.

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/wasi-master/dpylint](https://github.com/wasi-master/dpylint)

Discord: [Wasi Master#6969](https://discord.com/users/723234115746398219)

Email: [arianmollik323@gmail.com](mailto:arianmollik323@gmail.com)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* Cyrus from the official discord.py server
  * For the event idea

* Gnome from the official discord.py server
  * For the idea to check for aliases. e.g. ctx.channel.send instead of ctx.send

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/wasi-master/dpylint.svg?style=flat
[contributors-url]: https://github.com/wasi-master/dpylint/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/wasi-master/dpylint.svg?style=flat
[forks-url]: https://github.com/wasi-master/dpylint/network/members
[stars-shield]: https://img.shields.io/github/stars/wasi-master/dpylint.svg?style=flat
[stars-url]: https://github.com/wasi-master/dpylint/stargazers
[issues-shield]: https://img.shields.io/github/issues/wasi-master/dpylint.svg?style=flat
[issues-url]: https://github.com/wasi-master/dpylint/issues
[license-shield]: https://img.shields.io/github/license/wasi-master/dpylint.svg?style=flat
[license-url]: https://github.com/wasi-master/dpylint/blob/master/LICENSE.txt
[code-size-shield]: https://img.shields.io/github/languages/code-size/wasi-master/dpylint.svg?style=flat
[code-size-url]: https://github.com/wasi-master/dpylint
[say-thanks-badge]: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
[say-thanks-url]: https://saythanks.io/to/arianmollik323@gmail.com
[downloads-badge]: https://img.shields.io/pypi/dm/dpylint.svg?style=flat
[downloads-url]: https://pypistats.org/packages/dpylint
[version-badge]: https://img.shields.io/pypi/v/dpylint.svg
[version-url]: https://pypi.org/project/dpylint/#history
[test-badge]: https://img.shields.io/github/workflow/status/wasi-master/dpylint/Python%20application.svg?label=tests
[test-url]: https://github.com/wasi-master/dpylint/actions/workflows/python-app.yml
[build-badge]: https://img.shields.io/github/workflow/status/wasi-master/dpylint/Upload%20Python%20Package.svg?label=build
[build-url]: https://github.com/wasi-master/dpylint/actions/workflows/python-publish.yml
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
