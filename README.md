# esg_competition

All codes used for evaluation of our ESG metrics-pdfs downloading, pdf to txt converting, searching for important words in txt documents and then with name matching assigning company names with important values from one database to the second(initial) database.

To evaluate bonuses for (S,G) metrics we were working in order : splitter.js => pdfDownloader.py => toTXT.py => wordsSearching.py => nameMatcher.py.

For getting list of companies and their pledges that are ready for evaluating ratio score in G metric, we used order: htmlDownloader.py => nameMatcher.py.

For getting a dependence of the future CO_2 contribution with historical data of contribution we used: randomForest.py.

*(For finding when company joined CO_2 pledge we would use: => textStrip.py => wordsSearching.py => (if words are not enough we can check sentences of those words) => sentenceSplitter.py ). <= This wasn't trained enough
