Entirely documented notebook in order to load and prepare the dataset built for training / finetuning the t5-base text-to-text small language model, to correct movie titles from text paragraphs containing errors in movie titles.

1. Download title.basics.tsv from https://datasets.imdbws.com/ -> official imdb site for non-commercial datasets
2. Filter the titles by removing all NSFW titles -> IMPORTANT!
3. Save the filtered titles to filtered_titles.tsv
4. Run fill_imdb.py to build the dataset required for training T5-base model. The dataset will then contain two columns, OCR generated title (error) and Movie Title (actual corrected title)
5. Examine the jupyter notebook and run each cell in order to train and finetune the t5-base model
