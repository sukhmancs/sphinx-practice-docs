..  _chapter1:

Chapter 1: Introduction to C++ in Sphinx
=========================================

.. index::
   single: C++ Code
   single: Source Code Documentation

Introduction
------------

In this chapter, we will explore how to include C++ code snippets and document C++ classes using Sphinx.

Including C++ Code
------------------

With the ``.. code-block:: cpp`` directive, we can include C++ code snippets in our documentation. Here's an example:

.. code-block:: cpp 

  int main()
  {
    std::cout << "hello sphinx!\n";
    return 0;
  }

This is a simple C++ program that prints "hello sphinx!" to the console.

Source Code Documentation
-------------------------

We can use the ``.. doxygenclass::`` directive to document C++ classes. Here are some examples:

.. doxygenclass:: foo
  :project: SphinxExample
  :members:
  :private-members:

.. doxygenclass:: foo1
  :project: SphinxExample
  :members:
  :private-members:

.. doxygenclass:: foo2
  :project: SphinxExample
  :members:
  :private-members:

These directives pull in the documentation for the `foo`, `foo1`, and `foo2` classes from the Doxygen XML output.

Conclusion
----------

In this chapter, we learned how to include C++ code snippets and document C++ classes in Sphinx. In the next chapter, we will explore more advanced topics.