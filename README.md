## How to Use

1. Install conan: https://docs.conan.io/en/latest/installation.html
2. Add my bintray to remote list in order to find required packages: `conan remote add czoido-bintray https://api.bintray.com/conan/czoido/conan-packages`
3. Clone this repo: `git clone https://github.com/czoido/conan-waf-build-helper-consumer.git`
4. `cd conan-waf-build-helper-consumer\`
5. `conan source . --source-folder build`
6. `conan install . --install-folder build --build missing`
7. `conan build . --build-folder build`
