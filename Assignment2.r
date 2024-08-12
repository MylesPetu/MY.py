# Installing packages in r
install.packages("tidyverse")
install.packages("lubridate")
install.packages("dplyr")
install.packages("ggplot2")


# To load Packages
library(tidyverse)
library(lubridate)
library(dplyr)
library(ggplot2)

# Open csv file 
df <- read.csv("C:/Users/PetuMyles/Downloads/Myles Petu - Cohort 18 Student Test Data.csv")
colnames(df)

#QUESTION 1
#How activity has influeced scores across different subjects 
df1 <- df[c("Activity","Subject","Score")]
dfview <- tail(df1)
# View(dfview)

# Average Score For each Subject wrt Extracurricular Activity      
average_score <- df1 %>%
    group_by(Subject, Activity)%>%
    summarise(Average_Score = round(mean(Score)))
head(average_score) 


#plot of the avg score againts the subject wrt  activity (Bar Plot)
plot2 <-ggplot(average_score, aes(x = Activity, y = Average_Score, fill = Activity)) +
    geom_bar(stat = "identity", position = "dodge") +
    facet_wrap(~ Subject) +
    labs(title = "Average Scores for Each Subject per Extracurricular Activity",
            x = "Extracurricular Activity",
            y = "Average Score") +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5),
            axis.text.x = element_text(angle = 45, hjust = 1))
plot2




#QUESTION 2
#relationship between age and academic performance and how employment influenes this relationship 
df2 <- df[c("Age","Employment.Status","Score")]
dfview <- head(df2)
View(df2)


# Calculate the average score for each age and group by employment status
avg_scores <- df2 %>%
  group_by(Age, Employment.Status) %>%
  summarise(Average_Score = round(mean(Score)))
View(avg_scores)  

# Create the scatter plot
plot3 <-ggplot(avg_scores, aes(x = Age, y = Average_Score, color = Employment.Status)) +
  geom_point(size = 10) +
  labs(title = "Relationship between Age and Average Score, Colored by Employment Status",
       x = "Age",
       y = "Average Score",
       color = "Employment Status") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))
plot3  

# Create a scatter plot for each employment status
plot4 <-ggplot(df2, aes(x = Age, y = Score)) +
    geom_point(aes(color = Employment.Status), size = 3) +
    facet_wrap(~ Employment.Status) +
    labs(title = "Scatter Plots of Age vs. Score for Each Employment Status",
       x = "Age",
       y = "Score") +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5))
plot4


#Question 3
#average score for each household type and group by financial status
avg_scores <- df %>%
    group_by(Household, Financial.Status) %>%
    summarise(Average_Score = round(mean(Score)))
avg_scores  
View(avg_scores)

#Bar plot
plot5 <-ggplot(avg_scores, aes(x = Household, y = Average_Score, fill = Financial.Status)) +
    geom_bar(stat = "identity", position = position_dodge()) +
    labs(title = "Average Academic Performance by Household Type and Financial Status",
         x = "Household Type",
         y = "Average Score") +
    theme_minimal() 
plot5


Question4
#Average Academic Performance by Household Type and Scholarship Status combination
average_scores_scholarship <- df %>%
    group_by(Household, Scholarship.Status) %>%
    summarise(Average_Score = round(mean(Score)))
View(average_scores_scholarship)    

# Bar plot
plot6 <-ggplot(average_scores_scholarship, aes(x = Household, y = Average_Score, fill = Scholarship.Status)) +
    geom_bar(stat = "identity", position = position_dodge()) +
    labs(title = "Average Academic Performance by Household Type and Scholarship Status",
         x = "Household Type",
         y = "Average Score") +
    theme_minimal() 
plot6    


# How does gender affect academic performance across different financial statuses?
average_scores_gender <- df %>%
    group_by(Financial.Status, Gender) %>%
    summarise(Average_Score = round(mean(Score)))
View(average_scores_gender)   

# Bar plot
plot7 <-ggplot(average_scores_gender, aes(x = Financial.Status, y = Average_Score, fill = Gender)) +
    geom_bar(stat = "identity", position = position_dodge()) +
    labs(title = "Average Academic Performance by Financial Status and Gender",
        x = "Financial Status",
        y = "Average Score") +
    theme_minimal() 
plot7    
# the bar plot shows average academic performance of each gender and their financial status



