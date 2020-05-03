# Word Frequency Counter-Chinese

**Archive**

📦Chinese
 ┣ 📂data
 ┃ ┣ 📜1-2.txt
 ┃ ┣ 📜11-12.txt
 ┃ ┣ 📜3-4.txt
 ┃ ┣ 📜9-10.txt
 ┃ ┗ 📜....txt
 ┣ 📜CalStatistics_Data.py
 ┣ 📜output.xlsx
 ┣ 📜pre_data.txt
 ┗ 📜README.md

**Required Package**

```python
jieba
pandas
```

[jieba](https://github.com/fxsjy/jieba):Chinese text segmentation

[pandas](https://pandas.pydata.org/): Python Data Analysis Library

**Workflow**

1. Put all the text files requiring statistics in  `data/`
2. Insert blocked words at the end of `pre_data.txt`
3. `python CalStatistics_Data.py`
4. View words frequency in `output.xlsx`