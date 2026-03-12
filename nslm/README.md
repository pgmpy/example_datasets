The dataset is from the National Study of Learning Mindsets and is mentioned in the paper titled "Estimating Treatment Effects with Causal Forests: An Application" by Susan Athey and Stefan Wager.

The National Study of Learning Mindsets was a study conducted in some of the US public high schools. This dataset emulates that observational study with similar characteristics. It is designed to explore whether a small nudge from teachers at school could affect students' behaviour.

The variables are the following:

- schoolid: The ID of the schools which students participate in the experiment.
- Z: Whether a student/participant recieves intervention. 1 means yes, 0 means no.
- Y: The participants' score, which are taken after the experiment.
- S3: The participants' expectation of success. This is measured before the experiment is executed.
- C1: Student race/ethnicity
- C2: Student identified gender
- C3: Student first-generation status to go to college
- XC: School-level variable: the location of the school (i.e. rural, suburban, etc.)
- X1: School-level mean of students' fixed mindsets, reported before the experiment.
- X2: School test scores and college preparation for the previous four cohorts.
- X3: School racial/ethnic minority distribution
- X4: School poverty concentration
- X5: Total students in all four grade levels in the high school.

To learn further about the dataset: https://github.com/grf-labs/grf/tree/master/experiments/acic18
Paper reference:
Susan Athey, & Stefan Wager. (2019). Estimating Treatment Effects with Causal Forests: An Application.
