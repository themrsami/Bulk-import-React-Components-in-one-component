import os
import inflect

# Create an inflect engine
p = inflect.engine()

# Define the path to the current directory
current_dir = '.'

# Iterate over all subdirectories in the current directory
for root, dirs, files in os.walk(current_dir):
    # Get all .jsx files in the current directory, excluding 'page.jsx'
    jsx_files = [f for f in files if f.endswith('.jsx') and f != 'page.jsx']

    if jsx_files:  # Check if there are any .jsx files in the current directory
        imports = []
        for i, file in enumerate(jsx_files):
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                if 'export default' in content:
                    imports.append(f"import Component{p.number_to_words(i+1)} from './{file[:-4]}';")
                else:
                    imports.append(f"import {{ Component{p.number_to_words(i+1)} }} from './{file[:-4]}';")

        # Create the component
        component = f"""
'use client';
import React from 'react';
{'\n'.join(imports)}

const Page = () => {{
  return (
    <>
      <div className='flex flex-col gap-32 mx-auto bg-white'>
        {'\n'.join([f'<Component{p.number_to_words(i+1)} />' for i in range(len(jsx_files))])}
      </div>
    </>
  )
}}

export default Page;
"""

        # Write the component to a new page.jsx file in the current directory
        with open(os.path.join(root, 'page.jsx'), 'w') as f:
            f.write(component)
