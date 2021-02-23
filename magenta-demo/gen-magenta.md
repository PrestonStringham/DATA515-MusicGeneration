---
jupyter:
  jupytext:
    formats: ipynb,py:percent,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.0
  kernelspec:
    display_name: Python [conda env:midi-data515-mag] *
    language: python
    name: conda-env-midi-data515-mag-py
---

The following code is adapted from:

https://github.com/magenta/magenta/blob/master/magenta/models/melody_rnn/melody_rnn_generate.py


```python
import ast
import os
import time
```

```python
from magenta.models.melody_rnn import melody_rnn_config_flags
from magenta.models.melody_rnn import melody_rnn_model
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator
from magenta.models.shared import sequence_generator_bundle
```

```python
import note_seq
from note_seq.protobuf import generator_pb2
from note_seq.protobuf import music_pb2
```

```python
import tensorflow.compat.v1 as tf
```

```python
FLAGS = tf.app.flags.FLAGS
```

You will need a bundle file (aka `.mag` file). I use `basic_rnn.mag`, which you can obtain at the following URL:

http://download.magenta.tensorflow.org/models/basic_rnn.mag

Set the BUNDLE constant to the path to the bundle file.

```python
#
# Constants 
#
BUNDLE     = '/Users/carljparker/git/dss/data515-sw-design/project-data515/magenta/basic_rnn.mag'
OUTPUT_DIR = '/Users/carljparker/git/dss/data515-sw-design/project-data515/magenta/'
```

Get the bundle (`.mag`) file

The original code incorporates the `.hparams` values, but I have commented out that line below. When we attempt to parse the `.hparams` we get an error, presumably because we are not running from the command line. Commenting out this line should be okay because the default for the `.hparams` values is nothing.

The following print command shows you a description of each flag. I've included the description for `--hparams`.

    print( tf.app.flags.FLAGS )

    magenta.models.melody_rnn.melody_rnn_config_flags:
    
    --hparams: Comma-separated list of `name=value` pairs. For each pair, the
        value of the hyperparameter named `name` is set to `value`. This mapping is
        merged with the default hyperparameters.
        (default: '')

```python
bundle = sequence_generator_bundle.read_bundle_file(BUNDLE)

if bundle:
    config_id = bundle.generator_details.id
    config = melody_rnn_model.default_configs[config_id]
    #
    #  config.hparams.parse(FLAGS.hparams)
    #
else:
    raise( FileNotFoundError )

generator = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
      model=melody_rnn_model.MelodyRnnModel(config),
      details=config.details,
      steps_per_quarter=config.steps_per_quarter,
      checkpoint=None,
      bundle=bundle)
```

The following values come from the tutorial at:

https://www.twilio.com/blog/generate-music-python-neural-networks-magenta-tensorflow

```python
num_steps   = 128
num_outputs =  10
```

```python
qpm = note_seq.DEFAULT_QUARTERS_PER_MINUTE
```

```python
primer_melody = note_seq.Melody([60])
primer_sequence = primer_melody.to_sequence(qpm=qpm)

# Set the start time to begin on the next step after the last note ends.
if primer_sequence.notes:
    last_end_time = max(n.end_time for n in primer_sequence.notes)
else:
    last_end_time = 0
```

```python
seconds_per_step = 60.0 / qpm / generator.steps_per_quarter
total_seconds = num_steps * seconds_per_step
```

```python
generator_options = generator_pb2.GeneratorOptions()
generate_section = generator_options.generate_sections.add(
    start_time=last_end_time + seconds_per_step,
    end_time=total_seconds)
```

```python
# Make the generate request num_outputs times and save the output as midi
# files.
input_sequence = primer_sequence
output_dir = OUTPUT_DIR
date_and_time = time.strftime('%Y-%m-%d_%H%M%S')
digits = len(str(num_outputs))
for i in range(num_outputs):
    generated_sequence = generator.generate(input_sequence, generator_options)

    midi_filename = '%s_%s.mid' % (date_and_time, str(i + 1).zfill(digits))
    midi_path = os.path.join(output_dir, midi_filename)
    note_seq.sequence_proto_to_midi_file(generated_sequence, midi_path)
```

```python

```
