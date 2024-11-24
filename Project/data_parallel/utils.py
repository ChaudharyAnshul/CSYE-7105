import nltk
import numpy as np
import logging
from datetime import datetime
import os
import nltk
from collections import Counter
import numpy as np
import os
import logging
from datetime import datetime

def tokenize_and_build_vocab(sentences, min_occurrence_threshold=1):
    words = Counter()
    tokenized_sentences = []
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        tokenized_sentences.append(tokens)
        words.update([word.lower() for word in tokens])
    words = {k: v for k, v in words.items() if v > min_occurrence_threshold}
    words = sorted(words, key=words.get, reverse=True)
    words = ["_PAD", "_UNK"] + words
    word2idx = {o: i for i, o in enumerate(words)}
    idx2word = {i: o for i, o in enumerate(words)}
    return tokenized_sentences, word2idx, idx2word

def convert_sentences_to_indices(sentences, word2idx):
    return [[word2idx.get(word.lower(), 1) for word in sentence] for sentence in sentences]

def pad_input(sentences, seq_len):
    features = np.zeros((len(sentences), seq_len), dtype=int)
    for idx, review in enumerate(sentences):
        if len(review) != 0:
            features[idx, -len(review):] = np.array(review)[:seq_len]
    return features

def split_validation_test(sentences, labels, split_frac):
    split_idx = int(len(sentences) * split_frac)
    val_sentences, test_sentences = sentences[:split_idx], sentences[split_idx:]
    val_labels, test_labels = labels[:split_idx], labels[split_idx:]
    return val_sentences, val_labels, test_sentences, test_labels

def setup_logger(world_size):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f'training_{world_size}CPUs_{timestamp}.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )