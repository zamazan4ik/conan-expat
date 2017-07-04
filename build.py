from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="pix4d", channel="testing",
                                 upload="https://api.bintray.com/conan/pix4d/conan")
    builder.add_common_builds(shared_option_name="Expat:shared")
    builder.run()
