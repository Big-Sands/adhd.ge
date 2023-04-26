# ADHD.ge
თქვენს წინაშეა ADHD.ge საიტის source code. არსებობს რამდენიმე მიზეზი ამის განთავსების:
- თუ მე ვერ მოვახერხე ამ პროექტზე მუშაობა, მინდა მივცე სხვებს საშუალება პროექტის გაგრძელების
- გამჭვირვალობა
- კონტრიბუტორების მოზიდვა

ამ საიტის და პროექტის მიზანი არის და ყოველთვის იქნება საქართველოში მცხოვრები ADHD-ის მქონე ხალხის ინტერესების დაცვა.

# ADHD.ge
This is the source code of ADHD.ge. There are several reasons for open-sourceing this:
- If I can no longer work on this project, I want to give others the opportunity to continue the project
- Transparency
- Attracting contributors

The purpose of this site and project is and always will be to protect the interests of people with ADHD living in Georgia.

# How this works

+ The articles are written in markdown and placed in the `articles` directory.
+ `render.py` python script is used to convert the markdown to HTML, along with making use of `template.html` to generate `index.html` files ready to be used in production.
+ Don't forget to install python and the project dependencies, `pip3 install -r requirements.txt`

