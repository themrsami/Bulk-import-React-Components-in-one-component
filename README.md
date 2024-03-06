## Title: React Component Auto-Importer and Consolidator

**Description:**

This script automates the creation of a new React component (named `page.jsx`) that imports and renders multiple existing `.jsx` components found within subdirectories of the current working directory. It handles different export styles and generates appropriate import statements.

**Features:**

- Consolidates multiple React components into a single "Page" component.
- Automatically generates import statements for each component.
- Handles components with both default and named exports.
- Excludes a specified file (`page.jsx`) from the import process.

**Installation:**

This script is intended to be used directly within a Node.js environment. No specific installation is required.

**Usage:**

1. Save the script as a `.py` file (e.g., `auto_import.py`).
2. Open a terminal or command prompt and navigate to the directory containing the script and your `.jsx` components.
3. Run the script using the following command:

```bash
python auto_import.py
```

**Example:**

Assuming you have three `.jsx` components named `Componentone.jsx`, `Componenttwo.jsx`, and `Componentthree.jsx` in subdirectories, running the script will create a new page.jsx file containing the following code

```bash
'use client';
import React from 'react';
import Component1 from './Componentone';
import Component2 from './Componenttwo';
import Component3 from './Componentthree';

const Page = () => {
  return (
    <>
      <div className='flex flex-col gap-32 mx-auto bg-white'>
        <Componentone />
        <Componenttwo />
        <Componentthree />
      </div>
    </>
  );
};
export default Page;
```

**Contributing:**

Feel free to submit pull requests for improvements or bug fixes.

**Please note:** This script modifies files in the current directory. Always back up your code before running the script.
