# GA4GH Variant Annotation Schema

The GA4GH Variant Annotation Schema, also called the *GA4GH Variant Annotation Core Information Model* is a data model that describes the structure of the metadata that the GA4GH expects for variant annotation tasks.

The core schema, or *data model* is written in the [linkml](https://github.com/linkml/linkml) framework. There are multiple artifacts that are generated from the linkml schema which can be found in [project](project/). The data model can also be used by importing the Python dataclasses that are generated [here](src/ga4gh_va_schema/datamodel/).

## Website

[https://sujaypatil96.github.io/ga4gh-va-schema](https://sujaypatil96.github.io/ga4gh-va-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [ga4gh_va_schema](src/ga4gh_va_schema)
    * [schema](src/ga4gh_va_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/ga4gh_va_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
