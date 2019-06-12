from conans import ConanFile, CMake, python_requires


base = python_requires("waf-build-helper/0.1@czoido/testing")


class ConsumerConan(base.get_conanfile()):
    settings = "os", "compiler", "build_type", "arch", "arch_build"
    name = "waf-build-helper-consumer"
    version = "0.2"
    generators = "Waf"
    exports = "wscript", "example.cpp"

    def requirements(self):
        self.requires("opencv/4.1.0@conan/stable")
        self.requires("WafGen/0.1@czoido/testing")

    def source(self):
        pass

    def build(self):
        waf = base.WafBuildEnvironment(self)
        waf.configure()
        waf.build()

    def imports(self):
        self.copy("*.dll", dst="build", src="bin")
        self.copy("*.dylib*", dst="build", src="lib")
