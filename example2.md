# Serialization of NDCube Classes to ASDF

# Google Summer of Code 2024

## Open Astronomy | SunPy (NDCube)

### Mentors: Daniel Ryan, Stuart Mumford, Brett Graham

### About Me

- Name: Piyush Sharma
- University: IIT Roorkee
- Major: Integrated BS-MS in Mathematics And Computing
- Timezone: IST (UTC +5:30)
- Contact Email: [`piyushsharma04321@gmail.com`](piyushsharma04321@gmail.com)
- Github Id: [`ViciousEagle03`](https://github.com/ViciousEagle03)
- Element.io Username: VEagle

### Platform Details

- OS: Ubuntu 22.04
- Editor: VS Code

### Background

I am a second-year undergraduate student at the [`Indian Institute of Technology, Roorkee`](https://en.wikipedia.org/wiki/IIT_Roorkee), majoring in
Mathematics and Computing. I have been programming for the past three years, primarily using
Python, along with proficiency in Java, C/C++, and JavaScript. Python has been instrumental in my
development, and I'm comfortable with frameworks like Flask and Django.

####

I have a few Python projects hosted on my [`GitHub`](http://www.github.com/ViciousEagle03) account, which I believe reflect my ongoing journey
and dedication to the language. [`[Relevant Project]`](https://github.com/ViciousEagle03/AIR_DART_2.0)

### Contribution/Pull Requests in SunPy/NDCube/Astropy

- https://github.com/astropy/astropy/pull/15985 [Merged]
- https://github.com/sunpy/sunpy/pull/7453 [Merged]
- https://github.com/sunpy/ndcube/pull/666 [Open]
- Assisted with issue #663 in sunpy/ndcube repository

### Approach to the project

The ndcube package is a SunPy-affiliated package that provides a collection of objects for representing
and manipulating data and world coordinates simultaneously. As of now, ndcube doesn't support saving an
NDCube object to a file and load an NDCube from a file.

`This document proposes to add the feature of saving any NDCube object to an ASDF file format
and then be able to load the NDCube object back in`. ASDF is chosen as the file format as it is well
suited to accommodating the complex metadata requirements of modern scientific data. Unlike FITS,
ASDF offers a hybrid text and binary format that addresses these challenges by providing a hierarchical
metadata structure, human-editable content, and efficient storage of binary data. Also, ASDF design
allows for the adoption of new conventions for storing complex metadata in a highly structured
manner. Incorporating ASDF serialization into NDCube will enhance its flexibility and compatibility,
enabling the storage of richer metadata structures.

Efforts were made to implement a save method for NDCube objects in the issue [`#111`](https://github.com/sunpy/ndcube/issues/111), aiming to write them to FITS files. However, the APE-14 API did not provide a generalized way to serialize gWCS to FITS and get the same gWCS object when we deserialize. Instead, serialization of gWCS to the ASDF format
was proposed as a solution. This involved developing a method to serialize FITS WCS objects to ASDF, as ASDF was identified as the primary serialization option for gWCS.

There were discussion regarding the serialization of FITS WCS objects to ASDF in issue [`#9735`](https://github.com/astropy/astropy/issues/9735). Initial attempts to add serialization support were made in the **astropy.io.misc.asdf module**. However, since the module will be [`removed`](https://github.com/astropy/asdf-astropy#:~:text=The%20astropy.io.misc.asdf%20module%20will%20be%20removed%20in%20a%20future%20version%20of%20astropy.) in future versions of Astropy, this proposal aims to incorporate serialization support through the [`asdf-astropy`](https://github.com/astropy/asdf-astropy) plugin instead and aims to address the limitations
imposed by the APE-14 API and enable the serialization of NDCube objects with gWCS and astropy.wcs.WCS representation to a more flexible and compatible format.

## Breakdown of the project

The document outlines the objectives in the subsequent sections:

### Basic serialization

The primary objective initially is to enable the serialization of basic attributes to ASDF, where `.data` is a
numpy array and `.wcs` is a gwcs.WCS object. Converters for the NDCube class will be defined to
achieve this goal, implementing the [`to_yaml_tree`](https://asdf.readthedocs.io/en/latest/asdf/extending/converters.html#:~:text=passed%20to%20other-,to_yaml_tree,-methods%20in%20other) method, which takes an NDCube object and returns a YAML representation of it. Additionally, a tag URI will be designated to the converter class to identify
the specific object type it handles. The resulting YAML representation will be validated by a schema designed for the basic NDCube object.

### `The schema design`

The schema will serve to validate and standardize the structure of an NDCube object when stored in a
YAML file. The structure of the schema would need to comply with the [`JSON Schema Draft 4`](https://json-schema.org/specification-links#draft-4). To ensure the schema designed for NDCube is valid and adheres to the ASDF schema specifications I would add a custom meta-schema. To uniquely identify the schema I would assign an ID to it and provide a title and description to document its purpose and content. To associate the type of object with the schema, the
type validators need to be set to NDCube. The properties validator will initially contain the basic
attributes of NDCube, but it will be updated to account for extra properties and metadata as we
progress with the project.

Leveraging existing Converters for converting gwcs.WCS objects to YAML format, the `.wcs` attribute can
be passed as a nested complex object in the [`to_yaml_tree`](https://asdf.readthedocs.io/en/latest/asdf/extending/converters.html#:~:text=passed%20to%20other-,to_yaml_tree,-methods%20in%20other) method. Similarly, a tag will be assigned to
the schema to uniquely identify it during serialization. To support deserialization I would implement
the [`from_yaml_tree`](https://asdf.readthedocs.io/en/latest/asdf/extending/converters.html#:~:text=other%20calls%20to-,from_yaml_tree,-methods%2C%20except%20where) method to reconstruct an NDCube object with the passed YAML data.

Now, for serialization of NDCube objects to ASDF, it would require the compulsory attributes `.data` and
`.wcs`. However, I will extend this support to include additional world coordinates associated with pixel
axes governed by the ExtraCoords class and to incorporate extra information related to the NDCube
object, governed by the GlobalCoords class. Thus, I will define the Converter class for these as well and
implement the [`to_yaml_tree`](https://asdf.readthedocs.io/en/latest/asdf/extending/converters.html#:~:text=passed%20to%20other-,to_yaml_tree,-methods%20in%20other) and [`from_yaml_tree`](https://asdf.readthedocs.io/en/latest/asdf/extending/converters.html#:~:text=other%20calls%20to-,from_yaml_tree,-methods%2C%20except%20where) methods to convert the ExtraCoords and GlobalCoords
instances into a YAML file, supporting the construction of these objects back from a valid YAML file,
respectively. The schema for the NDCube object would then be adjusted to include optional properties
for ExtraCoords and GlobalCoords.

To associate each Converter class with the serialization process we would need to register the
Converter Classes with the ASDF using the extension URIs.

### Extend Serialization Support for WCS Objects

Unlike gWCS objects, astropy.wcs.WCS does not support serialization to asdf, to enable the serialization, I would implement the necessary methods in the Converter class and ensure proper schema design within the asdf-astropy package to add the support.

We would also need to designate URI tags to both the Converter Class and schema design, this would help to distinguish between astropy.wcs.WCS object and gwcs.WCS object during the serialization process of the NDCube object and the correct Converter to associate with the associated WCS object. This part of the project aims to broaden the scope of serialization support to include astropy.wcs.WCS
class and other relevant WCS wrapper classes.

Now the next phase would be to enable the manipulated NDCube object to be able to be saved to ASDF format and this would require converters to be written for various WCS wrapper classes, that is, SlicedLowLevelWCS, ResampledLowLevelWCS, CompoundLowLevelWCS, and ReorderedLowLevelWCS
to ensure when an NDCube object is manipulated or transformed then the serialization process takes into account of the changes and accurately save the object to ASDF file. The extension class will need to be written to incorporate this serialization logic into the ASDF ecosystem.

I would then restructure the schema of the NDCube object to take into account the added support for various types of WCS objects. The test suite would then be expanded to cover a diverse range of scenarios, ensuring comprehensive support for different WCS objects.

### Advanced Serialization for Complex NDCube Objects

Once the basic serialization of the ndcube.NDCube object with various WCS representations is implemented, the next step would involve extending the serialization process to include optional properties/metadata like mask, uncertainty, and PSF. A well-structured Schema and a Converter must
be added for the astropy.nddata.NDUncertainty class within [`asdf_astropy`](https://github.com/astropy/asdf-astropy) to preserve the metadata
during serialization. After registering the Converter, I would update the schema for NDCube to include the properties of metadata as optional properties. This development will enable NDCube to efficiently
handle complex metadata configurations, enabling accurate conversion to ASDF format.

NDCubeSequence, a class for handling multiple contiguous NDCube objects, and NDCollection, a container class for unordered grouping of NDCube or NDCubeSequence instances. Both of the classes depend on NDCube instances. Leveraging the already developed serialization methods for
ndcube.NDcube objects, Converters for NDCubeSequence, and NDCollection would utilize compound serialization. Additionally, Schema definitions for these classes would reference the schema of the NDCube class, ensuring consistency within the serialization framework. After this, the converters will be registered to the ASDF library. Extend the existing test suite for NDCube to cover NDCollection and
NDCubeSequence classes.

For clarity and maintainability, I would be in parallel documenting, and detailing the Converter Classes
and schema design, and tags and URIs associated with each corresponding Converter Classes would
be written along with tests to validate the functionality of the implementation.

![image](https://github.com/sunpy/sunpy/assets/117067393/5d77be0f-a330-48d3-9221-2191ae2c9897)

## Timeline of the Project

### Community Bonding Period(May 1 - May 26)

During the community bonding period, having developed a fair bit of knowledge of asdf serialization I aim to contribute to solving some issues within the [`asdf-astropy`](https://github.com/astropy/asdf-astropy) repository to help me get acquainted with the working knowledge of Schema design and Converters. I would discuss with the mentors if any change needs to be made to the proposal, regarding the timeline and weekly project goals. I will be taking my end-term examination till 8th May, so I will be fairly busy until then. I plan to start working on
the initial phase of the project and develop a prototype of Schema and Converter Class for the ndcube.NDCube object to discuss the prototype and get feedback on whether the prototype aligns with the project requirements. I will also try to complete my pending [PR] by the end of the Community Bonding Period.

To ensure efficient implementation I would try to commit every subsequent change I make to the WIP PR to keep my work on track and provide visibility for mentors to offer guidance if I veer off course from my goals.

### Week 1 (May 27th - June 2nd)

- Discuss the structure of the schema design of NDCube with its .wcs attribute as gwcs.WCS.
- Make a WIP PR to the ndcube repository to add the support of serialization to ASDF.
- Implement the Converter for the NDCube class.
- Documentation for the same.

### Week 2 (June 3rd - June 9th)

- Design the schema for GlobalCoords and ExtraCoords classes.
- Write Converters for both the classes.
- Make schemas installable as ASDF library resources for easy access.
- Implement the Extension class to register the Converters.
- Documentation and tests for the same.

### Week 3 (June 10th - June 16th)

- Review and refine the schemas for NDCube, GlobalCoords, and ExtraCoords.
- Further testing to ensure smooth interaction within the ASDF ecosystem.
- Document the implemented Converters and schema.

### Week 4 (June 17th -June 23rd)

- Ensure the complete implementation of the ASDF extension infrastructure to the ndcube package.
- Test serialization and deserialization of NDCube objects using ASDF.
- Extend the existing test suite with additional examples of saving and loading NDCube objects backed
  by different gwcs.WCS objects.
- Discuss with mentors regarding the existing ASDF extension framework, and whether any
  enhancement or adjustment is needed to optimize the framework's efficiency.

### Week 5 (June 24th - June 30th)

- Begin designing the schema and implement the Converters for astropy.wcs.WCS within the
  [`asdf-astropy`](https://github.com/astropy/asdf-astropy) package.
- Implement the Extension class to register the Converter written within asdf-astropy.
- Complete any remaining task before 1st evaluation.

### Week 6 (July 1st - July 7th)

- Complete any remaining task before 1st evaluation.
- Design the schema and implement Converters for the remaining WCS wrapper classes,
  SlicedLowLevelWCS, ResampledLowLevelWCS, CompoundLowLevelWCS, and
  ReorderedLowLevelWCS classes.
- Documentation and test for the same.

## Midterm Evaluation

### Week 7- Week 8 (July 9th - July 21th)

- Discuss with mentors regarding the progress and address any issues raised during the midterm
  evaluation.
- Get the PR merged for ndcube to support the existing serialization of NDCube objects.
- Implement the Extension class to register the converters for all the WCS wrapper classes.
- Document the support enabling the saving of manipulated NDCube objects to ASDF format.
- Test serialization and deserialization of manipulated NDCube objects using ASDF.

### Week 9 (July 22nd - July 28th)

- Buffer week for leftover tasks.
  Week 10 (July 29th - August 4th)
- Implement Converters and schemas for the astropy.data.NDUncertainity class in asdf-astropy.
- Documentation and tests for the same.
- Write the Extension class to register the Converters.
- Test serialization and deserialization of NDCube object with optional properties set.

### Week 10 (July 29th - August 4th)

- Implement Converters and schemas for the astropy.data.NDUncertainity class in [`asdf-astropy`](https://github.com/astropy/asdf-astropy).
- Documentation and tests for the same.
- Write the Extension class to register the Converters.
- Test serialization and deserialization of NDCube object with optional properties set.

### Week 11 - Week 12 (August 5th - August 18th)

- Design the schema and implement the Converters for NDCubeSequence and NDCollection.
- Documentation and tests for the same.
- Implement the Extension classes to register the Converters.
- Test serialization and deserialization of NDCubeSequence and NDCollection instances.

### Week 13(August 19th - August 26th)

- Write up documentation for remaining tasks.
- Write documentation about the usage of the project.
- Ensure all the documentation related to the project is properly organized.
- Get feedback on the overall project from the mentors.
- Complete any leftover task.

## Final Evaluation!

## GSoC

### Q) Have you previously participated in GSoC?

No

### Q) Are you applying to other projects?

No, I am solely applying for this project within this organization.

### Q) How much time do you plan to invest in the project before, during, and after the Summer of Code?

My end-term examinations are scheduled from May 1st to May 8th. However, since this period aligns with the Community Bonding phase, I don’t think this will be an issue as the coding period starts on May 26th.
From May 8th to July 20th, I will have college vacations, so I would easily be able to dedicate 40 hours/week to the project given its medium-sized(175 Hours) scope, also I do not have any major commitments during my summer vacations. Even after classes resume on July 21st, I am confident that I will still be able to allocate over 35 hours per week, as there will be no examinations or major commitments.

### Q) Are you eligible to receive payments from Google?

Yes, I am eligible to receive payment from Google.
