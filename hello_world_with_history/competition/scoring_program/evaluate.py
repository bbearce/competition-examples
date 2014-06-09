#!/usr/bin/env python
import sys
import os
import os.path

input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')
history_dir = os.path.join(input_dir, 'history')

if not os.path.isdir(submit_dir):
    print "%s doesn't exist" % submit_dir

if os.path.isdir(history_dir):
    # read all phases
    phases = {}

    for folder, sub_folders, files in os.walk(history_dir):
        # phases[1] = [1, 2, 3] -- phase 1 with 3 submissions #1, 2, 3
        phases[folder] = sub_folders
    
    print phases

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, 'scores.txt')
    output_file = open(output_filename, 'wb')

    truth_file = os.path.join(truth_dir, "truth.txt")
    truth = open(truth_file).read()

    submission_answer_file = os.path.join(submit_dir, "answer.txt")
    submission_answer = open(submission_answer_file).read()

    if truth == submission_answer:
        output_file.write("correct:1")
    else:
        output_file.write("correct:0")

    output_file.close()
