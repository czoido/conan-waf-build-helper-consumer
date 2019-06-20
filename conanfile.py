from conans import ConanFile, python_requires


base = python_requires("waf-build-helper/0.1@czoido/testing")


class ConsumerConan(base.get_conanfile()):
    settings = "os", "compiler", "build_type", "arch", "arch_build"
    name = "waf-build-helper-consumer"
    version = "0.2"
    generators = "Waf"
    exports = "wscript", "example.cpp"
    requires = "opencv/4.1.0@conan/stable", "WafGen/0.1@czoido/testing"
    build_requires = "waf/2.0.17@czoido/testing"

    def source(self):
        pass

    def build(self):
        waf = base.WafBuildEnvironment(self)
        waf.configure()
        waf.build()

    def imports(self):
        self.copy("*.dll", dst="build", src="lib")
        self.copy("*.dylib*", dst="build", src="lib")
        self.copy("*.so*", dst="build", src="lib")
