from airflow import DAG, macros
from airflow.operators.bash import BashOperator
from datetime import timedelta,datetime
import pendulum


default_args = {
    'owner' : 'john'
    ,'retries' : 5
    ,'retry_delay': timedelta(minutes=1)
}


with DAG(
    dag_id = 'daily_ambience_comparison'
    ,description = 'this renders predefined rmarkdown reports daily, and pushes them to a github.io project'
    ,start_date=datetime(2025,3,10,tzinfo=pendulum.timezone("America/Denver"))
    ,catchup = True
    ,schedule_interval = '00 7 * * *'
) as dag:
    
    report_render = BashOperator(
        task_id = 'index_rmd'
        ,bash_command = "cd {{ var.val.r_dir_ambComp }}; Rscript renderer.R"
    )

    mv_results = BashOperator(
        task_id='mv_to_github'
        ,bash_command = "cd {{ var.val.r_dir_ambComp }}; mv -f index.md dailyReport.html {{ var.val.githubIO_dir }}ambience_comparison/; mv -f images/*.png {{ var.val.githubIO_dir }}ambience_comparison/images/"
    )

    git_push = BashOperator(
        task_id = "update_githubIO"
        ,bash_command = "cd {{ var.val.githubIO_dir }}ambience_comparison/; git add index.md dailyReport.html images/*.png; git commit -m 'updates results on {{ macros.ds }}'; git push origin master"
    )

    report_render >> mv_results >> git_push 
