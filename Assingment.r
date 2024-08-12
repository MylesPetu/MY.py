# Installing packages in r
# install.packages("tidyverse")
# install.packages("lubridate")
# install.packages("dplyr")
# install.packages("ggplot2")


# To load Packages
library(tidyverse)
library(lubridate)
library(dplyr)
# library(ggplot2)

#Student Data Frame
Data_Frame <- data.frame(
    name = c("Ayoukunle", "Ayobami", "Sophia", "Noah", "Olivia", "William", "Liam", "James", "Isabella", "Benjamin", "Charlotte", "Elijah", "Ameeda", "Aisha", "Evelyn", "Mason", "Harper", "Ethan", "Abigail", "Awesome"),
    age = c(13, 23, 29, 19, 24, 30, 35, 22, 30, 26, 18, 16, 29, 21, 22, 14, 16, 25, 34, 33),
    class = c("100 Level", "200 Level", "300 Level", "200 Level", "400 Level", "100 Level", "300 Level", "200 Level", "400 Level", "300 Level", "500 Level", "100 Level", "300 Level", "400 Level", "100 Level", "500 Level", "300 Level", "100 Level", "300 Level", "100 Level"),
    score = c(92, 78, 61, 47, 39, 85, 98, 55, 100, 80, 67, 35, 90, 72, 43, 25, 88,80,50,25)
)


# Conditional Columns 
df1 <- Data_Frame %>%
  mutate(grade = case_when(
    score >= 85 ~ "A",
    score >= 75 & score < 85 ~ "B",
    score >= 65 & score < 75 ~ "C",
    score >= 50 & score < 65 ~ "D",
    score < 50 ~ "F"
  ))  
View(df1)

df2 <- df1 %>%
  mutate(age_group = case_when(
    age >=13 & age<=19 ~ "Teen",
    age >=20 & age<=25 ~ "Young Adult",
    age >25 ~ "Adult"
  ))
 View(df2)



#dataset containing class and number of students in each class

class_frequency <- Data_Frame%>% 
    group_by(class)%>%
    reframe(Count = n())     
class_frequency

class_frequency <- Data_Frame %>%
    count(class) 
     # Modifies the headings of the table  
    names(class_frequency) <- c("Year_of_Study", "Count") 

View(class_frequency)



#Ploting the distribution 



age_group_counts <- df2 %>%
  count(age_group) 

ggplot(age_group_counts, aes(x = age_group, y = n, fill = age_group)) +
  geom_bar(stat = "identity", linetype = "dashed") +  # Adjust fill color as desired
  labs(title = "Distribution of Students by Age Group",
       x = "Age Group",
       y = "Number of Students"
       ) +
  theme_bw()


#Random Selection 

names <- c("Idris", "Berbatov", "Paul")
#no of rows 
students <- 20
#an empty data frame
student_data <- data.frame(name = character(), age = integer(), grade = character())

for (i in 1:students) 
{
    random_name <- sample(names, 1)
    age <- round(runif(1, min = 13, max = 100))
    grade <- function(score) {
    if (score >= 85) return("A")
    else if (score >= 75 & score < 85) return("B")
    else if (score >= 65 & score < 75) return("C")
    else if (score >= 50 & score < 65) return("D")
    else return("F")
  }
#generates a score and assigns a grade  
  score <- round(runif(1, min = 45, max = 100))
  random_grade <- grade(score)
  
# Adds rows to the data frame
  student_data <- rbind(student_data, data.frame(name = random_name, age = age, grade = random_grade))
}
View(student_data)

write.csv(Data_Frame,"C:/Users/PetuMyles/Desktop/table.csv",row.names = FALSE)
