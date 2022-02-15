:py:mod:`build_tree`
====================

.. py:module:: build_tree


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   build_tree.TreeNode
   build_tree.BinarySearchTree




Attributes
~~~~~~~~~~

.. autoapisummary::

   build_tree.mytree


.. py:class:: TreeNode(key, val, left=None, right=None, parent=None)

   .. py:method:: hasLeftChild(self)


   .. py:method:: hasRightChild(self)


   .. py:method:: isLeftChild(self)


   .. py:method:: isRightChild(self)


   .. py:method:: isRoot(self)


   .. py:method:: isLeaf(self)


   .. py:method:: hasAnyChildren(self)


   .. py:method:: hasBothChildren(self)


   .. py:method:: spliceOut(self)


   .. py:method:: findSuccessor(self)


   .. py:method:: findMin(self)


   .. py:method:: replaceNodeData(self, key, value, lc, rc)



.. py:class:: BinarySearchTree

   .. py:method:: length(self)


   .. py:method:: __len__(self)


   .. py:method:: put(self, key, val)


   .. py:method:: _put(self, key, val, currentNode)


   .. py:method:: __setitem__(self, k, v)


   .. py:method:: get(self, key)


   .. py:method:: _get(self, key, currentNode)


   .. py:method:: __getitem__(self, key)


   .. py:method:: __contains__(self, key)


   .. py:method:: delete(self, key)


   .. py:method:: __delitem__(self, key)


   .. py:method:: remove(self, currentNode)



.. py:data:: mytree
   

   

