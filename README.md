# Autogen_Skills
A collection of autogen skills for use with locally run models

**SDtxt2img.py**
- Give an Autogen agent the ability to generate images in stable diffusion. Requires the Stable Diffusion WebUI (AUTOMATIC1111/Forge/etc). WebUI must be started with the --api command line argument.
- For now, generation parameters (seed, sampler, scale, etc) are all modified directly in the code. The code also includes a generic negative prompt which can be changed. Right now there is no option to choose the SD Checkpoint used, so it will just use the last one loaded in.