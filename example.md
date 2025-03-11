# Improve sunkit-image

## Personal Details

Name: Jayraj Dulange <br>
University: Indian Institute of Technology Gandhinagar <br>
Time Zone: IST (GMT+5:30) <br>
Email: jayraj.jayraj@iitgn.ac.in <br>
Github username: Deus1704 <br>
Element.io username: [Deus1704](https://github.com/Deus1704) <br>

## Personal Background

Hey there, I'm Jayraj Dulange, a sophomore at [Indian Institute of Technology, Gandhinagar](https://en.wikipedia.org/wiki/IIT_Gandhinagar) majoring in Electrical Engineering. I'm genuinely interested in open-source, especially in image processing, machine learning, and development in general. For the past three years I’ve been using Python for tasks like web scraping, automation, and scientific computing. I've used Git & GitHub for version control and collaborating with others in almost every project for the last 2 years. Recently, I led a team of 5 developers in creating the TEDxIITGandhinagar [website](https://tedxiitgandhinagar.in), which has now surpassed 2000 unique page views!

## Relevant Projects

- Wrote a python [script](https://github.com/Deus1704/Identification_of_Word_Inside_Audio_Waveform) from scratch to identify the Hindi words present in an audio and subsequently annotate the audio waveforms with the actual words.
- [Implemented](https://github.com/Deus1704/Super_Resolution_Using_RFF) a machine learning model for Super Resolution using Random Fourier Features and Linear regression.

## Open Source History

Being new to open source, I had participated in [Winter of Code 2023](https://winterofcode.com/), an open source contribution challenge similar to Hacktoberfest, to gain experience. I got 2 pull requests merged during the month-long event.[[1]](https://github.com/OWASP-BLT/BLT/pull/1656) [[2]](https://github.com/OWASP-BLT/BLT/pull/1697)

## Contributions to SunPy community

Below is the list of my top contributions that I have made to SunPy and sunkit-image.

### My submitted pull requests

1. [sunkit-image] [implements stara #195](https://github.com/sunpy/sunkit-image/pull/195) [Draft]
2. [sunpy] [fixes the solar_rotate_coordinate() #7526](https://github.com/sunpy/sunpy/pull/7526) [Open]
3. [sunpy] [Adds a warn when using both assume_spherical_screen() and propagate_with_solar_surface() context managers with reproject_to() #7437](https://github.com/sunpy/sunpy/pull/7437) [Open]
4. [sunpy] [Implemented the vector transformation from one frame to another #7452](https://github.com/sunpy/sunpy/pull/7452) [Draft]
5. [sunpy] [Fixes naxis update issue #7522](https://github.com/sunpy/sunpy/pull/7522) [Merged]

In addition to my contributions, my [discussions](https://matrix.to/#/!MeRdFpEonLoCwhoHeT:matrix.org/$171051692038115PSSwy:matrix.org?via=matrix.org&via=openastronomy.org&via=cadair.com) on the matrix chat have led to few constructive discoveries. For instance, we identified that the sunpy-soar conda feedstock was out of date, causing issues for many users.

## GSoC & I

### **Have I previously participated successfully in GSoC? When? With which project?**

No, I haven’t.

### **Are you also applying to other projects?**

No, I’m not.

### **Are you eligible to receive payments from Google?**

Yes, I am.

### **How much time do you plan to invest in the project before, during, and after the Summer of Code?**

Before GSoC, I'll be dedicating ~10 hours per week due to mandatory institute lectures. During summer vacation (May-July), I can commit ~35 hours per week which is indeed inline with the expectation of 175 hours(~18 - 22 hours per week) for medium sized projects. From late July, my availability may drop to ~20 hours per week for 1-2 weeks due to intern test rounds and travel. I'll discuss these dates with mentors in advance and proceed based on their approval. After this period, I'll resume full commitment. Post-GSoC, I'll remain active to address issues and assist new contributors.

## Project Details

### Overview

The sunkit-image package, associated with SunPy, provides several tools for processing images related to solar physics. Currently, there are several unresolved issues that need attention. These include restructuring modules, incorporating gallery examples, and transferring other image processing methods from the SunPy core. These issues are majorly high effort and hence have been open for a long time. I believe that these must be addressed on a priority basis.

### Issue Breakdown and Approach

Let us now break down every issue mentioned in the list and discuss what all will be delivered by the end of the coding period. Adhering to the sunpy guidelines and mentor’s suggestion of not working on any GSoC listed issue before the actual selection of the candidate I haven’t created a pull request for any of these issues.

### [Declass ASDA #42](https://github.com/sunpy/sunkit-image/issues/42) :

Over the years there have been many attempts to solve this issue, but they haven’t been successful in completing it end to end due to some issues at their end. The ASDA is currently implemented using a class-based structure, which contrasts with the function-based structure used by the other image processing methods in sunkit-image. Therefore, to ensure consistency across all methods, it's necessary to complete this task. Having read the ASDA [paper](https://arxiv.org/pdf/1804.02931.pdf), I propose to declass this module along with the proper documentation of the mathematical expressions used.

### [Clean up sunkit_image.trace API #134](https://github.com/sunpy/sunkit-image/issues/134) :

This matter has been formally closed, with confirmation from Nabil that it has been removed from the list of issues slated for resolution in the GSoC project. You can find further details [here](https://github.com/sunpy/sunkit-image/issues/134#issuecomment-2002554083).

### [ASDA has no gallery example #45](https://github.com/sunpy/sunkit-image/issues/45) :

There is a WIP example that is discussed [here](https://github.com/sunpy/sunkit-image/issues/45). After finishing the previous declass task, my primary goal would be to ensure:

- That all the TODOs mentioned in this example are fulfilled with appropriate explanations
- The output obtained is the desired and infer based on the output.

### [Refactor the coalignment module](https://github.com/sunpy/sunkit-image/issues/83) :

Currently, this module, which includes code from `sunpy.image.coalignment` and `sunpy.physics.solar_rotation`, has an inconsistent API(for example, it is non obvious for a user to choose which coalignment method they want to apply on their map sequence.) and redundant code(for example, the repetition of array creation code for storing both arcseconds and pixel shifts ). Refactoring it will streamline the user readability, facilitate the integration of new image alignment methods, simplify debugging, and ultimately elevate the quality of the repository. The top level proposed structure of the Coalignment module is outlined below,
![Screenshot from 2024-03-29 06-19-27](https://github.com/sunpy/sunpy/assets/117574289/85dfa79a-1243-4ecb-8924-91757f82caf1)
In the updated code, users can simply call `mapsequence_coalign`, passing the map sequence. They have the option to specify different algorithms by setting the `method` parameter, or they can obtain the shifts without applying them directly to the mapSequence by setting `apply_shift` to false. This simplification of the API enhances usability and offers greater flexibility for users. <br>

Additionally, there are some algorithmic issues, like the `mapsequence_coalign_by_rotation` highlighted in [this](https://github.com/sunpy/sunkit-image/issues/186) matter and discussed by Albert. Based on his suggestions I’ve drafted a modified algorithm that, based on my understanding, takes into account the full `PC_ij` matrix and the required changes that follow for correct conversion in this [gist](https://gist.github.com/Deus1704/980f962ef2848cf32647558330ccd770).

### [Add a coalignment example to the gallery #103](https://github.com/sunpy/sunkit-image/issues/103) :

Currently there are two examples in the gallery that demonstrate the use of coalignment module. I propose adding another practical example to the sunkit_image gallery that demonstrates co-alignment of images from different instruments, specifically AIA and EIS. This would require additional understanding of the [image registration](https://scikit-image.org/docs/stable/api/skimage.registration.html) method present in the skimage.

### [Add persistence transform example to the gallery](https://github.com/sunpy/sunkit-image/issues/76) :

Persistence transform is a really effective way to visualize the evolution of solar structures. However, the example gallery lacks relevant examples. There has been a [pull request](https://github.com/sunpy/sunkit-image/pull/137) that dealt with this issue, but again wasn’t completed. I propose that we adopt that pull request as the mentors have already invested significant time in reviewing and discussing the necessary changes, modify on top of it based on the unaddressed reviews. By doing so, we can efficiently address the issue and finalize the example.

### [Failing test test_multiscale_gaussian #96](https://github.com/sunpy/sunkit-image/issues/96) :

I have already looked in the cause of the issue, discussed and solved this issue before in this [pull request](https://github.com/sunpy/sunkit-image/pull/193) and confirmed with Nabil that this issue is no longer included in the GSoc list of issues that are to be dealt with.

### [Figure out what from SunPy core can be moved here #5](https://github.com/sunpy/sunkit-image/issues/5) :

While the sunpy core does contain some visualization tools, these are primarily utilized within other sunpy modules. As such, it's not immediately clear which functions or methods could be beneficially relocated to sunkit-image. I believe that a conversation with the mentors about their specific expectations and requirements would be more productive than us proposing potential functions to relocate. This would ensure that any relocation aligns with their vision and the overall project goals. I have indeed discussed some methods that could potentially be relocated [here](https://github.com/sunpy/sunkit-image/issues/5#issuecomment-2028118567).

## [Bonus] Apart from the issues mentioned above, few others that I believe could be completed.

### [Add noise gating #64](https://github.com/sunpy/sunkit-image/issues/64) :

[This](https://github.com/drzowie/image-noise-gate) image processing technique aims to improve image quality by eliminating noise from image sequences, a challenge that caught my attention due to its potential to significantly enhance signal-to-noise ratio (SNR) and effective exposure time. Given my background in electrical engineering, I'm familiar with Fourier Transforms, a key component of this method, which adds to my excitement about tackling this task. While optimistic about this issue, I'm mindful of the time constraints and challenges that may arise during its completion, hence would like to discuss and work on this if time permits.

### [Add limb darkening correction #68](https://github.com/sunpy/sunkit-image/issues/68):

[Limb Darkening Correction](https://academic.oup.com/mnras/article/318/2/387/1025415) (LDC) is a vital preprocessing step in numerous astrophysical disciplines, notably in the exploration of stellar atmospheres. It compensates for the limb darkening effect, a phenomenon where the disk of a star appears progressively dimmer towards the edges as compared to the center. I believe that this method needs to be present in sunkit-image because it not only enhances the accuracy of the observational data but also enriches our understanding of stellar characteristics. There have been [two](https://github.com/sunpy/sunpy/pull/3728) implementations in the past but again haven’t been completed. Given the complexity of this task, I propose addressing it during a GSoC period to ensure its successful completion. This focused effort will provide the necessary time and resources to enhance sunkit-image effectively.

## Timeline

### Pre-GSOC period (Before May 1)

- Go through the ASDA paper again and understand all the terms in depth.
- Ask questions
- Complete my draft pull request in sunpy and sunkit-image.

### Community Bonding Period (May 1 - 26)

During the community bonding period, I plan to participate in the weekly SunPy meetings to immerse myself in the development community and its practices. I also aim to delve deeper into understanding pytest and figure tests. I intend to deepen my understanding of <b>Noise-gating</b> and <b>LDC</b> by studying their respective papers. Furthermore, I will engage in discussions with mentors to identify additional open issues in the sunkit-image repository as discussed in this proposal as a <b>bonus</b> that could potentially be addressed during the coding period, provided there is sufficient time. I’ll discuss with the sunpy community about which transformation/methods they wish to relocate from the sunpy core to sunkit-image. To further increase transparency in my work, I’ll start adding weekly progress to my <b>blog</b>.

### Week 1 (May 27th - June 2nd)

- Declass ASDA, ensuring proper documentation of the <b>mathematical expressions</b> utilized within.
- Initialize a pull request and receive feedback and integrate them in the code.
- Complete the reading and understanding of the current WIP ASDA example.

### Week 2 (June 3rd - June 9th)

- Begin with adding explanations to the ASDA example and get feedback on it.
- Create a draft pull request and keep it updated with the latest changes so as to keep track of the actual work.

### Week 3 (June 10th - June 16th)

- Finish the example and address any suggestions or issues.
- Start with the refactoring of the co-alignment module according to the <b>proposed structure</b>.

### Week 4 (June 17th -June 23rd)

- Complete the refactoring. Update the gallery examples based on the new method of accessing the coalignment API.
- Initiate the composition of the new coalignment example.

### Week 5 (June 24th - June 30th)

- Complete the coalignment example, have working figure tests implemented and get them reviewed.
- Begin writing the <b>persistence</b> transform example.

### Week 6 (July 1st - July 7th)

- Finish the persistence transform example, initialize a pull request and seek reviews and suggestions.
- Address any remaining task before first evaluation.
- Initiate <b>performance profiling</b> of frequently utilized functions, starting with coalign using match template, as it relies on the `match_template` from `skimage`.
- Develop detailed <b>performance reports</b> for each evaluated function.

### _Midterm Evaluation_

### Week 7- Week 8 (July 9th - July 21st)

- Discuss with the mentors regarding progress and address any issue raised during the midterm evaluation.
- Initiate the refinement and extension of the existing <b>Limb Darkening Correction (LDC)</b> implementation. Collect the data for an appropriate figure test.
- Write the required figure tests and a numerical test.
- Initialize a pull request and seek reviews and suggestions.

### Week 9 (July 22nd - July 28th)

- Finish the LDC implementation, update the sunkit-image documentation.
- Begin the transfer of the finalized methods from the sunpy core to sunkit-image.
- Ensure that there are appropriate redirections to the sunkit-image documentation, in the sunpy documentation.

### Week 10 (July 29th - August 4th)

- Complete the relocation process of the methods. Document the changes.
- Finish performance profiling, identify bottlenecks.
- Compile performance reports for identified functions, pinpoint bottlenecks, and propose efficiency enhancements.

### Week 11 (August 5th - August 11th)

- Implement the proposed enhancements. Create a pull request and get reviews.
- Initiate the implementation of the Noise-gating method. Consult with mentors regarding the choice between importing or developing the algorithm.
- Write unit and figure tests for noise-gating based on the sunpy mapsequence.

### Week 12 (August 12th - August 18th)

- Complete the implementation along with tests.
- Add a gallery example to demonstrate the use of noise-gating method.
- Initialize a pull request and get reviews.

### Week 13 (August 19th - August 26th)

- Buffer week before the final evaluation.
- Final update on the blog summarizing all the work done up to this week.

### _Final Evaluation_
