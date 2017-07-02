from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="piponazo", channel="testing",
                                 upload="https://api.bintray.com/conan/piponazo/piponazo",
                                 remotes="https://api.bintray.com/conan/conan/conan-center")
    builder.add_common_builds(shared_option_name="Expat:shared")
    builder.run()
