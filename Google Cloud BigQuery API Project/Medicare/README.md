# MEDICARE Project

This program reads one of the public data Medicare datasets and grabs data for
analysis. We start by using the inpatient_charges_2015 dataset. We'll use a SQL query to 
select the information from the dataset that we want to look at and eventually analyze.

## The Medicare Public Database

Medicare is the national health insurance program (single payer) in the United States
administered by the Centers for Medicare and Medicade Services (CMS). It provides health
insurance for Americans aged 65 and over. It also provides health insurance to younger
people with certain disabilities and conditions. In 2017 it provided health insurance to
over 58 million individuals.

With 58 million individuals in the system, Medicare is generating a huge amount of big
data every year. Google and CMS teamed up to put a large amount of this data on the
BigQuery public database so you can take a peek at this data and do some analytics
without trying to load it all on your local machine.

Below are the output results of the script:

![Record Returned](images/MQPic.png)

We found 112 records total from Great Falls. You can go back and change the query in the 
program to see results from a different city and state.