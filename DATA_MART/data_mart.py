import pandas as pd

# Load DataFrames (adjust paths as needed)
users_df = pd.read_csv('path/to/prep_Users.csv')
departments_df = pd.read_csv('path/to/prep_Departments.csv')
skills_df = pd.read_csv('path/to/prep_Skills.csv')
courses_df = pd.read_csv('path/to/prep_Courses.csv')
course_departments_df = pd.read_csv('path/to/prep_CourseDepartment.csv')
skill_departments_df = pd.read_csv('path/to/prep_SkillsDepartment.csv')
course_users_df = pd.read_csv('path/to/prep_CourseUsers.csv')
skill_users_df = pd.read_csv('path/to/prep_SkillUsers.csv')

# Step 1: Create Dimension Tables

# DimUser
dim_user = users_df[['user_id', 'first_name', 'last_name', 'account_type', 'department_name', 'createdAt', 'updatedAt']]

# DimDepartment
dim_department = departments_df[['department_id', 'department_name']]

# DimSkill
dim_skill = skills_df[['skill_id', 'skill_name']]

# DimCourse
dim_course = courses_df[['course_id', 'course_name', 'course_desc', 'course_creator', 'createdAt', 'updatedAt']]

# Step 2: Create Fact Tables

# FactSkillUser: Merge skill_users with dim_user, and dim_skill to get full information
fact_skill_user = skill_users_df.merge(dim_user, on='user_id', how='inner')\
                                .merge(dim_skill, on='skill_id', how='inner')\
                                .merge(skill_departments_df, on='skill_id', how='inner')\
                                .merge(dim_department, on='department_id', how='inner')

# FactCourseUser: Merge course_users with dim_user, and dim_course to get full information
fact_course_user = course_users_df.merge(dim_user, on='user_id', how='inner')\
                                  .merge(dim_course, on='course_id', how='inner')\
                                  .merge(course_departments_df, on='course_id', how='inner')\
                                  .merge(dim_department, on='department_id', how='inner')

# Step 3: Save the Dimension and Fact Tables to CSV
dim_user.to_csv('./data/mart_DimUser.csv', index=False)
dim_department.to_csv('./data/mart_DimDepartment.csv', index=False)
dim_skill.to_csv('./data/mart_DimSkill.csv', index=False)
dim_course.to_csv('./data/mart_DimCourse.csv', index=False)
fact_skill_user.to_csv('./data/mart_FactSkillUser.csv', index=False)
fact_course_user.to_csv('./data/mart_FactCourseUser.csv', index=False)

print("Data mart creation complete.")
