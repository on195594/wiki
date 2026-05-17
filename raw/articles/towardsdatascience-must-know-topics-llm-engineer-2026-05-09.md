---
title: The Must-Know Topics for an LLM Engineer
author: Aliaksei Mikhailiuk
source_type: article
source_url: https://towardsdatascience.com/the-must-know-topics-for-an-llm-engineer/
publisher: Towards Data Science
published_at: 2026-05-09
captured_at: 2026-05-17
extraction: browser_dom_article_main
status: raw
tags: [llm, engineering, architecture]
---

# The Must-Know Topics for an LLM Engineer

Source URL: https://towardsdatascience.com/the-must-know-topics-for-an-llm-engineer/

Extraction note: Direct HTTP extraction was blocked or summary-like; this raw capture uses browser DOM extraction from `article/main`. The source file used for ingestion was `/home/lin/Downloads/tds-llm-engineer-source.md`.

Gemini summary path: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260517-155459-The-Must-Know-Topics-for-an-LLM-Engineer-259012-488087680-summary.md`

## Raw article text

LARGE LANGUAGE MODELS
The Must-Know Topics for an LLM Engineer

From tokenisation to evaluation :  how modern language models actually work in practice

Aliaksei Mikhailiuk
May 9, 2026
31 min read
Share
Image generated with Gemini

Large Language Models (LLMs) have quickly become the foundation of modern AI systems — from chatbots and copilots to search, coding, and automation. But for engineers transitioning into this space, the learning curve can feel steep and fragmented. Concepts like tokenization, attention, fine-tuning, and evaluation are often explained in isolation, making it hard to form a coherent mental model of how everything fits together.

I ran into this firsthand when moving from computer vision to LLMs. In a short span of time, I had to understand not just the theory behind transformers, but also the practical realities: training trade-offs, inference bottlenecks, alignment challenges, and evaluation pitfalls.

This article is designed to bridge that gap.

Rather than diving deep into a single component, it provides a structured map of the LLM engineering landscape — covering the key building blocks you need to understand to design, train, and deploy real-world LLM systems.

We’ll move from the fundamentals of how text is represented, through model architectures and training strategies, all the way to inference optimization, evaluation, and system-level considerations and practical consideration like prompt engineering and reducing hallucinations.

Image by the Author.

By the end, you should have a clear mental framework for how modern LLM systems are built — and where each concept fits in practice.

Converting letters to numbers
Stages transforming text into the vectors that are fed into the LLMs. Image by the Author.
Tokenisation

When feeding data to a model, we can’t just feed it letters or words directly — we need a way to convert text into numbers. Intuitively, we might think of assigning each word in the language a unique number and feeding those numbers to the model. However, there are hundreds of thousands of words in the English language, and training on such a vast vocabulary would be infeasible in terms of memory and efficiency.

So what can be done instead? Well, we could try encoding letters, since there are only 26 in the English alphabet. But this would lead to problems as well — models would struggle to capture the meaning of words from individual letters alone, and sequences would become unnecessarily long, making training difficult.

A practical solution is tokenization. Instead of representing language at the word or character level, we split text into the most frequent and useful subword units. These subwords act as the building blocks of the model’s vocabulary: common words appear as whole tokens, while rare words can be represented as combinations of smaller subwords.

A common algorithm for that is Byte-Pair-Encoding (BPE). BPE starts with individual characters as tokens, then repeatedly merges the most frequent pairs of tokens into new tokens, gradually building up a vocabulary of subword units until a desired vocabulary size is reached.

At this stage each token is assigned a unique number — its ID in the vocabulary.

Embeddings

After we have tokenized the data and assigned token IDs, we need to attach semantic meaning to these IDs. This is achieved through text embeddings — mappings from discrete token IDs into continuous vector spaces. In this space, words or tokens with similar meanings are placed close together, and even algebraic operations can capture semantic relationships (for example: embedding(queen) — embedding(woman) + embedding(man) ≈ embedding(king)).

Generally, embedding layers are trained to take token IDs as input and produce dense vectors as output. These vectors are optimized jointly with the model’s training objective (e.g., next-token prediction). Over time, the model learns embeddings that encode both syntactic and semantic information about words, subwords, or tokens. Popular embedding models are: word2vec, glove, BERT.

Positional encoding

Generally, LLMs are not inherently aware of the structure of language. Natural language has a sequential nature — word order matters — but at the same time, tokens that are far apart in a sentence may still be strongly related. To capture both local order and long-range dependencies, we inject positional information of the tokens into each embedding.

There are several common to positional approaches:

Absolute positional encodings — Fixed patterns, such as sine and cosine functions at different frequencies, are added to token embeddings. This is simple and effective but may struggle to represent very long sequences, since it does not explicitly model relative distances.
Relative positional encodings — These represent the distance between tokens instead of their absolute positions. A popular method is RoPE (Rotary Positional Embeddings), which encodes position as vector rotations. This approach scales better to long sequences and captures relationships between distant tokens more naturally.
Learned positional encodings — Instead of relying on fixed mathematical functions, the model directly learns position embeddings during training. This allows flexibility but can be less generalizable to sequence lengths not seen in training.
Model Architecture
Encoder-Decoder architecture. Image by the Author.

After the data is tokenized, embedded, and enriched with positional encodings, it is passed through the model. The current state-of-the-art architecture for processing textual data is the transformer architecture, whose core is base on the attention mechanism. A transformer typically consists of a stack of transformer blocks:

Multi-Head Attention: Enables the model to focus on different parts of the input sequence simultaneously, capturing diverse context. It calculates Queries (Q), Keys (K), and Values (V) to define word relationships.
Position-wise Feed-Forward Network (FFN): A fully connected network applied to each position independently, adding non-linearity.
Residual Connections: Short-cut connections that help gradients flow during training, preventing information loss.
Layer Normalization: Normalizes the input to stabilize training.
Attention
Attention Mechanism. Image by the Author

Introduced in the paper called Attention Is All You Need, in attention, every token is projected into three vectors: a query (what it’s looking for), a key (what it offers), and a value (the actual information it carries). Attention works by comparing queries to keys (via similarity scores) to decide how much of each value to aggregate. This lets the model dynamically pull in relevant context based on content, not position.

Multi-head attention runs several attention mechanisms in parallel, each with its own learned projections. Think of each “head” as focusing on a different relationship (e.g., syntax, coreference, semantics). Combining them gives the model a richer, more nuanced understanding than a single attention pass.

There are several types of attention mechanism that vary based on its purpose: self-attention, masked self-attention and cross-attention. 

Self-attention operates within a single sequence, letting tokens attend to each other (e.g., understanding a sentence). Masked self-attention is similar to self-attention with a key difference in that attention only sees past tokens, without observing the future ones. 
Cross-attention connects two sequences, where one provides queries and the other provides keys/values (e.g., a decoder attending to an encoded input in translation). The key difference is whether context comes from the same source or an external.

Standard attention compares every token with every other token, leading to quadratic complexity O(n2). As sequence length grows, computation and memory usage increase rapidly, making very long contexts expensive and slow. This is one of the main bottlenecks in scaling LLMs and an active field of research —for example through being selective about what tokens attend to what tokens.

Architecture types

Language modeling tasks are built using one of the following transformer architectures:

Encoder-only models — Each token can attend to every other token in the sequence (bidirectional attention). These models are typically trained with masked language modeling (MLM), where some tokens in the input are hidden, and the task is to predict them. This setup is well-suited for classification and understanding tasks (e.g., BERT).
Decoder-only models — Each token can attend only to the tokens that come before it in the sequence (causal or unidirectional attention). These models are trained with causal language modeling, i.e., predicting the next token given all previous ones. This setup is ideal for text generation (e.g., GPT).
Encoder–Decoder models — The input sequence is first processed by the encoder, and the resulting representations are then fed into the decoder through cross-attention layers. The decoder generates an output sequence one token at a time, conditioned both on the encoder’s representations and its own previous outputs. This setup is common for sequence-to-sequence tasks like machine translation (e.g., T5, BART).
Next token prediction and output decoding

Models are trained to predict the next token — this is done by outputting a probability distribution over all possible tokens in the vocabulary. Output of the model is the logit which is then passed through the softmax to predict the probability of the next token in the vocabulary.

In the most straightforward approach, we could always choose the token with the highest probability (this is called greedy decoding). However, this strategy is often suboptimal, since the locally most likely token does not always lead to the globally most coherent or natural sentence.

To improve generation, we can sample from the probability distribution. This introduces diversity and allows the model to explore different continuations. Moreover, we can branch the generation process by considering multiple candidate tokens and expanding them in parallel.

Several popular decoding strategies used in practice are:

Beam search: Instead of following a single greedy path, beam search keeps track of the top n candidate sequences (beams) at each step, expanding them in parallel and ultimately selecting the sequence with the highest overall probability.
Top-k sampling: At each step, only the k most probable tokens are considered, and one is sampled according to their probabilities. This avoids sampling from the long tail of very unlikely tokens.
Top-p sampling (nucleus sampling): Instead of fixing k, we select the smallest set of tokens whose cumulative probability is at least p(e.g., 0.9). Then we sample from this set, dynamically adjusting how many tokens are considered depending on the shape of the distribution.

To control how “flat” or “peaked” the probability distribution is LLMs use a temperature parameter. A low temperature (<1) makes the model more deterministic, concentrating probability mass on the most likely tokens. A high temperature (>1) makes the distribution more uniform, increasing randomness and diversity in the generated output.

Training stages
Image generated with Gemini

LLM training typically has two stages: pre-training, where the model learns general language patterns such as grammar, syntax, and meaning from large-scale data, and fine-tuning, where it is adapted to perform specific tasks, such as following instructions or answering questions in a desired format and later on refines outputs to align with human preferences and safety constraints. 

This progression moves from capability (what the model can do) to alignment (what the model should do).

Pre-training

Pre-training is the most computationally expensive stage of LLM training because the model must learn from extremely large and diverse datasets. This typically involves hundreds of billions to trillions of tokens drawn from sources such as web pages, books, articles, code, and conversations.

To guide decisions about model size, training time, and dataset scale, researchers use LLM scaling laws, which describe how these factors relate and help estimate the optimal setup for achieving strong performance.

Data pre-processing is a crucial step because raw text can significantly degrade LLM performance if used directly. Training data comes from many sources, each with its own challenges that must be cleaned and filtered.

Web pages often contain boilerplate content such as ads, navigation menus, headers, and footers, along with formatting noise from HTML, CSS, and JavaScript. They may also include duplicated pages, spam, low-quality text, or even harmful content.
Books can introduce issues like metadata (publisher details, page numbers, footnotes), OCR errors from digitization, and repetitive or stylistically inconsistent passages. In addition, copyright restrictions require careful filtering and licensing compliance.
Code datasets may include auto-generated files, duplicated repositories, excessive comments, or boilerplate code. Licensing constraints are also important, and low-quality or buggy code can negatively impact training if not removed.

To address these challenges, datasets are typically filtered by language and quality, and imbalances across sources are corrected through data augmentation or re-weighting.

Suprevised fine-tuning

In supervised fine-tuning, we typically do not update all model parameters. Instead, most of the pretrained weights are kept frozen, and only a small number of additional parameters are trained. This is done either by adding lightweight adapter modules or by using parameter-efficient methods such as LoRA, while training on a small sub-set of filtered and clean set of data.

Low Rank Adaptation (LoRA) is one of the most widely used approaches. Instead of updating the full weight matrix, LoRA learns two smaller low-rank matrices, A and B, whose product approximates the update to the original weights. The pretrained weights remain fixed, and only A and B are trained. This makes fine-tuning far more efficient in terms of memory and compute while still preserving performance. (See also: practical LoRA training techniques and best practices.) 
Beyond LoRA, other parameter-efficient methods include prefix tuning, where a small set of trainable “virtual tokens” is added to the input and optimized during training, and adapter layers, which are small trainable modules inserted between existing transformer blocks while the rest of the model remains frozen.

At a higher level, supervised fine-tuning itself is the stage where we teach the model how to behave on a specific task using high-quality labeled examples. This typically includes:

Dialogue data: curated human–human or human–AI conversations that teach the model how to respond naturally in interactive settings.
Instruction data: prompt–response pairs that train the model to follow instructions, answer questions, and perform reasoning or task-specific outputs.

Together, these techniques align a pretrained model with the behavior we actually want at inference time.

Reinforcement learning

After supervised fine-tuning teaches the model what to do, reinforcement learning is used to refine how well it does it, especially in open-ended or subjective tasks like dialogue, reasoning, and safety. 

Unlike supervised learning with fixed targets, RL introduces a feedback loop: model outputs are evaluated, scored, and improved over time. This makes RL a key tool for aligning models with human preferences. In practice, it helps: encourage helpful, harmless, and honest behaviour, reduce toxic, biased, or unsafe outputs and improve instruction-following and conversational quality.

Because alignment data is smaller but higher quality than pre-training data, RL acts as a fine-grained steering mechanism, not a source of new knowledge.

A common paradigm is Reinforcement Learning from Human Feedback (RLHF), which typically involves three steps:

Collect preference data: As the gold standard humans rank multiple model responses to the same prompt (e.g., which is more helpful or safe), producing relative preferences rather than absolute labels, however, in some cases, stronger models are used to generate preference data or critique weaker models, reducing reliance on expensive human labeling. In practice, combining human and automated feedback allows scaling while maintaining quality.
Train a reward model (RM): A separate model is trained to score responses according to human preferences. Given a prompt and a candidate response, the reward model assigns a scalar score representing how good the response is according to human judgment.
Optimize the policy (the LLM): The language model, is then trained to maximize the reward signal, i.e., to generate outputs humans are more likely to prefer.

Optimizing the policy (LLM) is often tricky — RL might destroy learnt knowledge, or the model might collapse to predicting one plausible output that would generate maximum reward without diversity. Several algorithms are used to perform this optimization and address the issues:

Proximal Policy Optimization (PPO): PPO updates the model while constraining how far it can move from the original policy in a single step, preventing instability or degradation of language quality. An excellent video explantion of the PPO can be found here.
Direct Preference Optimization (DPO): bypasses the need for an explicit reward model. It directly optimizes the model to prefer chosen responses over rejected ones using a classification-style objective, simplifying the pipeline and reduces training complexity.
Group Relative Policy Optimization (GRPO): A variant that compares groups of outputs rather than pairs, improving stability and sample efficiency by leveraging richer comparative signals.
Kahneman-Tversky Optimization (KTO): KTO incorporates asymmetric preferences (e.g., penalizing bad outputs more strongly than rewarding good ones), which can better reflect human judgment in safety-critical scenarios.

RL for language models can be broadly categorized into online and offline based on how data is collected and used during training:

Offline RL (dominant today): The model is trained on a fixed dataset of interactions. There is no further interaction with humans or the environment during optimization: once preference data is collected and the reward model is trained, policy optimization (e.g., PPO or DPO) is performed on this static dataset.
Online RL: The model continuously interacts with the environment (e.g., users or human annotators), generating new outputs and receiving fresh feedback that is incorporated into training. This creates a dynamic feedback loop where the model can explore and improve iteratively.

Reasoning-aware RL (e.g., RL through Chain-of-Thought)
RL can also be applied to improve reasoning. Instead of only rewarding final answers, the model can be rewarded for producing high-quality intermediate reasoning steps (chain-of-thought). This encourages more structured, interpretable, and reliable problem-solving behavior.

Hallucination in LLMs
Image generated with Gemini

Even LLMs trained on factually correct data have a tendency to produce non-factual completions, also known as hallucinations. This happens because LLMs are probabilistic models that are predicting the next token conditioned on the training data corpus and generated tokens so far and are not guaranteed to produce exact matching with the data trained on. There are, however, ways to minimise the effect of hallucinations in LLMs:

Retrieval Augmented Generation (RAG): Incorporate external knowledge sources at inference time so the model can retrieve relevant, factual information and ground its responses in verified data, reducing reliance on potentially outdated or incomplete internal knowledge. RAG can be fairly complex from the engineering perspective and typically consists of:

Chunking: splitting documents into smaller, manageable pieces before indexing them for retrieval. Good chunking balances context and precision: chunks that are too large dilute relevance, while chunks that are too small lose important context. 
Embedding: convert chunks of text into dense vector representations that capture semantic meaning. In RAG, both queries and documents are embedded into the same vector space, allowing similarity search to retrieve relevant content even when exact keywords don’t match. 
Retrieval: High-quality retrieval ensures that relevant, diverse, and non-redundant chunks are passed to the model, reducing hallucinations and improving factual accuracy. It depends on factors like embedding quality, chunking strategy, indexing method, and search parameters.
Reranking: A second-stage filtering step that reorders retrieved chunks using a more precise (often more expensive) model. While initial retrieval is optimized for speed, rerankers focus on relevance, helping prioritize the most useful context for generation. 

Training to say I don’t know: Explicitly teach the model to acknowledge uncertainty when it lacks sufficient information, discouraging it from generating plausible-sounding but incorrect statements.

Exact matching and post-evaluation: Use strict matching or verification against trusted sources or external model‑based verifiers and critics during completion or post-processing to ensure generated content aligns with factual references, particularly for sensitive or precise information.

Optimization
Image generated with Gemini

Training LLMs is a challenge in itself — training the model requires huge number of GPUs, as we need to store the model, gradients and parameters of the optimizer. However, inference is also a challenge — imagine having to serve millions of requests — user retention is higher if the models can infer the text fast and with high quality.

Training optimization

Training large models is typically done using stochastic gradient descent (SGD) or one of its variants. Instead of updating model parameters after every single example, we compute gradients on batches of data, which makes training more stable and efficient. In general, the larger the batch size, the more accurate the gradient estimate is, though extremely large batches can also slow convergence or require tuning.

For very large models such as LLMs, a single GPU cannot store all the parameters or process large batches on its own. To address this, training is distributed across multiple GPUs or even across clusters of machines. This requires carefully deciding how to split the workload — either by dividing the data, the model parameters, or the computation pipeline.

While distributed training has been studied extensively in deep learning, LLMs introduce unique challenges due to their enormous parameter counts and memory requirements. Several strategies have been developed to overcome these:

Data parallelism — Each GPU holds a copy of the model but processes different batches of data, with gradients averaged across GPUs.
Model parallelism — The model’s parameters are split across multiple GPUs, so each GPU is responsible for a part of the model.
Pipeline parallelism — Different layers of the model are assigned to different GPUs, and data flows through them like stages in a pipeline.
Tensor parallelism — Individual tensor operations (e.g., large matrix multiplications) are themselves split across multiple GPUs.
DeepSpeed / ZeRO — A library and set of optimization techniques for training large models efficiently, including partitioning optimizer states, gradients, and parameters to reduce memory usage.

Generally in these there are two parameters that we are trying to optimize — reduce across GPU communication (e.g. for gradient exchange), while also making sure that we fit meaningful data on the GPUs. Other techiques to reduce memory during training and gain some speedups include:

Gradient checkpointing: A memory-saving training technique that stores only a subset of intermediate activations during the forward pass and recomputes the rest during backpropagation. This trades extra compute for significantly lower GPU memory usage, enabling training of larger models or longer sequences.
Mixed precision training: Uses lower-precision formats (e.g., FP16 or BF16) for most computations while keeping critical values (like master weights or accumulations) in higher precision (FP32). This reduces memory usage and speeds up training, especially on modern GPUs with specialized hardware, with minimal impact on accuracy.
Inference Optimization
Distillation: Large models are often overparameterized, so we can train a smaller student model to mimic a larger teacher. Instead of learning only the correct outputs, the student matches the teacher’s full probability distribution — including less likely tokens — capturing richer relationships. This yields near-teacher performance in a much smaller, faster model.
Flash-attention: An optimized attention algorithm that computes exact attention while dramatically reducing memory usage. It avoids materializing the full attention matrix by tiling computations and fusing operations into a single GPU kernel, keeping data in fast on-chip memory. The result: significantly faster training and inference, especially for long sequences, and support for longer context lengths without changing the model.
KV-caching: During autoregressive generation, recomputing attention over past tokens is wasteful. KV-caching stores previously computed keys and values and reuses them for future tokens. This reduces generation complexity from quadratic to linear in sequence length, greatly speeding up long-form text generation.
Prunning: Neural networks are often overparameterized, so pruning removes redundant weights. This can be structured (removing entire neurons, heads, or layers) or unstructured (removing individual weights). In practice, structured pruning is preferred because it aligns better with hardware, making the speedups actually realizable.
Quantisation: Reduces numerical precision (e.g., from 32-bit floats to 8-bit integers) to shrink models and speed up computation. It lowers memory usage and improves efficiency on specialized hardware. Applied either after training or during training, it may slightly impact accuracy, but careful calibration minimizes this. Effective quantization also requires controlling value ranges (e.g., small activation magnitudes) to avoid information loss. 
Speculative decoding: Speeds up generation using two models: a small, fast draft model and a larger, accurate target model. The draft proposes multiple tokens ahead, and the target verifies them in parallel — accepting matches and recomputing mismatches. This allows generating multiple tokens per step instead of one.
Mixture of experts (MoE): Instead of activating all parameters for every token, MoE models use many specialized “experts” and a gating mechanism to select only a few per input. This enables massive model capacity without proportional compute cost. Notable examples include Switch Transformer, GLaM, and Mixtral.

A more detailed blog from NVIDIA for inference optimization would certainly be a great read if you would like to use some more advanced techniques.

Prompt engineering
Image generated with Gemini

Prompt engineering is a core part of working with LLMs because, in practice, the model’s behavior is not just determined by its weights but by how it is conditioned at inference time. The same model can produce dramatically different results depending on how instructions, context, and constraints are written.

Prompt engineering is not one-shot design — it’s iteration. Small changes in wording, ordering, or constraints can produce large behavior shifts. Treat prompts like code: test, measure, refine, and version-control them as part of your system.

What makes a strong prompt
Be explicit about the task, not just the topic: A weak prompt asks what you want (“Explain RAG”). A strong prompt specifies how you want it (“Explain RAG in 5 bullet points, focusing on failure modes, for a technical blog audience”). 
Separate instruction, context, and format: Clear prompts distinguish between what the model should do, what information it should use, and how the output should look. For example: instructions (“summarize”), context (retrieved text), and format (“JSON with fields X, Y, Z”). 
Use examples (few-shot prompting): Providing 1–3 examples of desired input-output behavior significantly improves reliability for complex tasks. This is especially useful for classification or formatting. 
Constrain output structure aggressively: If you need machine-readable or consistent output, define strict formats (e.g. JSON, schemas).
Control context, quality: More context isn’t always better. Irrelevant or noisy inputs degrade performance. Prioritize high-signal information, and in RAG systems, ensure retrieval is precise and filtered.
Practical considerations
Track prompt changes like code. Know who changed what, when, and why. This makes debugging and rollback possible.
Use templates where possible. Break prompts into reusable components (instructions, context slots, formatting rules). 
Use routing systems. Adjusting both the model selection and the prompt depending on the user requests.
Have structured testing. Run prompts against a fixed dataset and compare outputs using metrics or structured rubrics (correctness, completeness, style). 
Keep a human in the loop. For subjective qualities like clarity or reasoning, human reviewers are still the most reliable signal — especially for edge cases.
Maintain a test suite of critical examples, especially around safety.
Redteaming — and trying to break the defences that you’ve built are now an industry norm.
Evaluation
Image generated with Gemini

Large language models are used across a wide range of tasks — from structured question answering to open-ended generation — so no single metric can capture performance in every case. In practice, evaluation depends heavily on the problem you’re solving. That said, most approaches fall into a few clear categories, spanning both traditional metrics and LLM-based evaluators.

Regardless of the metrics used one of the metrics used the most important part of the evaluation is the reference anchor for what would be considered good model performance — the evaluation dataset. It needs to be diverse, clean, grounded in the reality and have the set of the target tasks for your model.

Conventional

These are typically collecting word level statisitics, simple to implement and quick, however have limitations — they do not understand semantics.

Levenstein distance — measures the minimum number of single-character edits (insertions, deletions, or substitutions) needed to transform one string into another.
Perplexity — measures how well a language model predicts a sequence, with lower values indicating the model assigns higher probability to the observed text.
BLEU — evaluates machine-translated text by measuring n-gram overlap between a candidate translation and one or more reference translations, emphasizing precision.
ROUGE — evaluates text summarization (and generation) by measuring n-gram and sequence overlap between a generated text and reference texts, emphasizing recall.
METEOR — evaluates generated text by aligning it with reference texts using exact, stemmed, synonym matches, balancing precision-recall.
LLM-based
BertScore: compares generated text to a reference using contextual embeddings from BERT. Instead of matching exact words, it measures semantic similarity in the embeddings space — how close the meanings are, making it strong at recognizing paraphrases and subtle wording differences. It is a good choice for summarization and translation tasks.
GPTScore: GPTScore uses a large language model to evaluate outputs based on reasoning — scoring things like correctness, relevance, coherence, or even style, without relying on reference. Its flexibility makes it ideal for subjective tasks without clear ground truth.
SelfCheckGPT: Prompts the same model to critique its own output, surfacing hallucinations, logical inconsistencies, or misleading claims. Useful in knowledge-heavy or reasoning tasks, where correctness matters but external verification may be expensive or slow.
Bleurt: A BERT-based metric fine-tuned for evaluation. It compares text using learned semantic representations and outputs a single quality score reflecting fluency, meaning preservation, and paraphrasing.
GEval: In GEval you prompt the model with a rubric (e.g., judge factuality or clarity), and it returns a score or detailed feedback. This makes it especially useful for subjective tasks where traditional metrics fail, offering evaluations that feel closer to human judgment.
Directed Acyclic Graph (DAG): approach breaks evaluation into a sequence of smaller, rule-based checks. Each node is an LLM judge responsible for one criterion, and the flow between nodes defines how decisions are made. This structure reduces ambiguity and improves consistency, especially when the task can be checked step by step.

LLM-based evaluation isn’t foolproof — it comes with its own quirks:

Bias: Judge models may favor longer answers, certain writing styles, or outputs that resemble their training data.
Variance: Because models are stochastic, small changes (like temperature) can lead to different scores for the same input.
Prompt sensitivity: Even minor tweaks to your evaluation prompt or rubric can shift results significantly, making comparisons unreliable.

Treat LLM evaluation as a system that needs calibration. Standardize prompts, test them rigorously, and watch for hidden biases.

Looking beyond traditional tasks — a class of metrics looks into evaluating RAG pipelines, that split the process of information retrieval into retrieval and generation steps — and rely on metrics specific to each step, and a class that looks into summarization metrcis.

If you would like to go deeper on LLM model evaluation, I would recommend this survey paper covering multiple methods.

When to use LLM-as-a-judge vs traditional metrics? 

Not every output can be neatly scored with rules. If you’re evaluating things like summarization quality, tone, helpfulness, or how well instructions are followed, rigid metrics fall short. This is where LLM-as-a-judge shines: instead of checking for exact matches, you ask another model to grade responses against a rubric.

That said, don’t throw out traditional metrics. When there’s a clear ground truth — like factual accuracy or exact answers. They’re fast, cheap, and consistent.

The best setups combine both: use traditional metrics for objective correctness, and LLM judges for subjective or open-ended quality.

Evaluation loops in production

Strong evaluation doesn’t rely on a single method — it’s layered:

Offline metrics: Start with labeled datasets and automated scoring to quickly filter out weak model versions.
Human evaluation: Bring in annotators or experts to assess nuance — realism, usefulness, safety and edge cases that metrics miss.
Online A/B testing: Finally, measure real-world impact — clicks, retention, satisfaction.

Once your system is live, evaluation doesn’t stop — it evolves. User interactions should be continuously logged, sampled, and reviewed. These real-world examples reveal failure cases and shifts in usage patterns. The more data you have logged from the model the more tools you would have for diagnostics: model embeddings, response, response time etc.

Even if your model itself remains unchanged, its behavior and performance can still shift over time. This phenomenon — known as behaviour drift — typically emerges gradually as external factors evolve, such as changes in user queries, the introduction of new slang, shifts in domain focus, or even small adjustments to prompts and templates. The challenge is that this degradation is often subtle and silent, making it easy to miss until it begins affecting user experience.

To catch drift early, pay close attention to both inputs and outputs. 

Input: Track changes in embedding distributions, query lengths, topic patterns, or the appearance of previously unseen tokens. 
Output: Track shifts in tone, verbosity, refusal rates, or safety-related flags. Beyond these direct signals, it’s also useful to monitor evaluation proxies over time — things like LLM-as-a-judge scores, user feedback (such as thumbs up or down), and task-specific heuristics on extened periods of time, taking in account user behaviour seasonality, triggering alerts when statistical differences exceed defined thresholds.
LLM Criticism

A common criticism of LLMs is that they behave like “information averages”: instead of storing or retrieving discrete facts, they learn a smoothed statistical distribution over text. This means their outputs often reflect the most likely blend of many possible continuations rather than a grounded, single “true” statement. In practice, this can lead to overly generic answers or confident-sounding statements that are actually just high-probability linguistic patterns.

At the core of this behavior is the cross-entropy objective, which trains models to minimize the distance between predicted token probabilities and the observed next token in data. While effective for learning fluent language, cross-entropy only rewards likelihood matching, not truth, causality, or consistency across contexts. It does not distinguish between “plausible wording” and “correct reasoning” — only whether the next token matches the training distribution.

The limitation becomes practical: optimizing for cross-entropy encourages mode-averaging, where the model prefers safe, central predictions over sharp, verifiable ones. This is why LLMs can be excellent at fluent synthesis but fragile at tasks requiring precise symbolic reasoning, long-horizon consistency, or factual grounding without external systems like retrieval or verification.

Summary

Building and deploying large language models is not about mastering a single breakthrough idea, but about understanding how many interdependent systems come together to produce coherent intelligence. From tokenization and embeddings, through attention-based architectures, to training strategies like pre-training, fine-tuning, and reinforcement learning, each layer contributes a specific function in turning raw text into capable, controllable models.

What makes LLM engineering challenging — and exciting — is that performance is rarely determined by one component in isolation. Efficiency tricks like KV-caching, FlashAttention, and quantization matter just as much as high-level choices like model architecture or alignment strategy. Similarly, success in production depends not only on training quality, but also on inference optimization, evaluation rigor, prompt design, and continuous monitoring for drift and failure modes.

Seen together, LLM systems are less like a single model and more like an evolving stack: data pipelines, training objectives, retrieval systems, decoding strategies, and feedback loops all working in concert. Engineers who develop a mental map of this stack are able to move beyond “using models” and start designing systems that are reliable, scalable, and aligned with real-world constraints.

As the field continues to evolve — toward longer context windows, more efficient architectures, stronger reasoning abilities, and tighter human alignment — the core challenge remains the same: bridging statistical learning with practical intelligence. Mastering that bridge is what shapes the work an LLM engineer.

Notable models in the chronological order

BERT (2018), GPT-1 (2018), RoBERTa (2019), SpanBERT (2019), GPT-2 (2019), T5 (2019), GPT-3 (2020), Gopher (2021), Jurassic-1 (2021), Chinchila (2022), LaMDA (2022), LLaMA (2023)

Liked the author? Stay connected!

If you liked this article share it with a friend! To read more on machine learning and image processing topics press subscribe!

Have I missed anything? Do not hesitate to leave a note, comment or message me directly on LinkedIn or Twitter!

WRITTEN BY

Aliaksei Mikhailiuk
See all from Aliaksei Mikhailiuk

Artificial Intelligence
Deep Learning
Editors Pick
Llm
Machine Learning

Share This Article

Share on Facebook
Share on LinkedIn
Share on X

Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.

Write for TDS
