import os
import huggingface_hub
import tqdm
import git

models = huggingface_hub.list_models(full=True,cardData=True, sort='downloads', direction=-1)
print(len(models))
path = os.path.dirname("../../git_repo/") # specify your path

success = 0
failed = 0
success_list = []
failed_list = []

username = '' # specify your huggingface username
password = '' # specify your huggingface password

for i in tqdm.tqdm(models):
    model_name = i.modelId
    try:
        if '/' in model_name:
            name = model_name.replace('/', ' ')
        else:
            name = model_name
        git.Repo.clone_from(url=f'https://{username}:{password}@huggingface.co/{model_name}', to_path=f'{path}{name}')
        success += 1
        success_list.append(model_name)
    except:
        failed += 1
        print(f'{model_name} failed')
        failed_list.append(model_name)
        pass

print(f'{success} success')
print(f'{failed} failed')
print(f'failed percentage: {failed/(success+failed)}')
