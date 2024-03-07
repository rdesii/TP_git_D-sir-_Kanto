
tasks = {"task1":"Setup de projet git","task2":"modification de tache","task3":"Stocker les taches dans l'ordinateur","task4":"Mise en service"}
def ajoute_tache(task_dict,nouvelle_tache, description):
	task_dict[nouvelle_tache]= description
def supprimer_tache(task_dict, tache_a_supprimer):
	if tache_a_supprimer in task_dict:
		del task_dict[tache_a_supprimer]
