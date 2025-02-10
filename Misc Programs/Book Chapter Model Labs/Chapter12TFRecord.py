# Raghav Sriram
# Period 6 ML Gabor
# Chapter 13

import pandas as pd
import tensorflow as tf

# Load the dataset
df = pd.read_csv("jobs_in_data.csv")

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
    if isinstance(value, type(tf.constant(0))):
        value = value.numpy()  # BytesList
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value.encode()]))

def _bytes_feature_no_encode(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

# serialize a row of the DataFrame into a tf.train.Example message
def serialize_example(work_year, job_title, salary_in_usd, employee_residence):
    feature = {
        'work_year': _int64_feature(work_year),
        'job_title': _bytes_feature(job_title),
        'salary_in_usd': _int64_feature(salary_in_usd),
        'employee_residence': _bytes_feature(employee_residence),
    }
    
    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))               #96
    return example_proto.SerializeToString()

# TFRecord file
def write_tfrecord(df, filename):
    with tf.io.TFRecordWriter(filename) as writer:
        for index, row in df.iterrows():
            example = serialize_example(
                work_year=row['work_year'],
                job_title=row['job_title'],
                salary_in_usd=row['salary_in_usd'],
                employee_residence=row['employee_residence']
            )
            writer.write(example)

tfrecord_file_path = '/mnt/data/jobs.tfrecord'

write_tfrecord(df, tfrecord_file_path)
print(f"TFRecord file created at: {tfrecord_file_path}")
