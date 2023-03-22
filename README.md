# GAN_ITMO
курс по GAN 2 семестр 2022/2023

Домашняя работа по CSP блокам.

Попробовала три архитектуры модели: 

1 - DCGAN результат: визуально лучший по качеству фейковых фото и графику лосса.

Ноутбук модели https://github.com/SLVmain/GAN_ITMO/blob/csp_gan/hw_3_csp_blocks/dcgan_faces_csp_blocks.ipynb

ClearML https://app.clear.ml/projects/1e1a4bbf56744c26b6eafa267510eeee/experiments/6c0b57ee203240769987fde34aaec815/output/execution

2 - DCGAN c CSP блоками в дискриминаторе с батч-нормализацией и без нормализации с батч нормализацией получен лучше результат, график лосса улучшился, но нужно еще дообучать, не хватило возможностей GPU доучить дальше.

Ноутбук модели https://github.com/SLVmain/GAN_ITMO/blob/csp_gan/hw_3_csp_blocks/discriminator_dcgan_csp_blocks.ipynb

ClearML https://app.clear.ml/projects/1e1a4bbf56744c26b6eafa267510eeee/experiments/2f78d059c9874bcdbbf158d36fd70850/output/execution

3 - DCGAN c CSP блоками в дискриминаторе и генераторе - не сошелся, генератор не смог научиться.

Ноутбук модели: https://github.com/SLVmain/GAN_ITMO/blob/csp_gan/hw_3_csp_blocks/generator_discrim_dcgan_csp_blocks.ipynb

clearml ссылка https://app.clear.ml/projects/1e1a4bbf56744c26b6eafa267510eeee/experiments/7db0cbe5d3eb496e90bb6ad0f01a8502/output/execution

4 - DCGAN c CSP блоками в генераторе - не сошелся, генератор не смог научиться.

Ноутбук модели https://github.com/SLVmain/GAN_ITMO/blob/csp_gan/hw_3_csp_blocks/generator_dcgan_csp_blocks.ipynb

ClearML https://app.clear.ml/projects/1e1a4bbf56744c26b6eafa267510eeee/experiments/6423f449671543949a0d8e0cc82dae39/output/execution


Ноутбук со всеми архитектурами моделей https://github.com/SLVmain/GAN_ITMO/blob/csp_gan/hw_3_csp_blocks/%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D1%8B_dcgan_csp_blocks.ipynb
