:py:mod:`escapeMaze`
====================

.. py:module:: escapeMaze


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   escapeMaze.Maze



Functions
~~~~~~~~~

.. autoapisummary::

   escapeMaze.searchFrom



Attributes
~~~~~~~~~~

.. autoapisummary::

   escapeMaze.PART_OF_PATH
   escapeMaze.TRIED
   escapeMaze.OBSTACLE
   escapeMaze.DEAD_END
   escapeMaze.myMaze


.. py:data:: PART_OF_PATH
   :annotation: = O

   

.. py:data:: TRIED
   :annotation: = .

   

.. py:data:: OBSTACLE
   :annotation: = +

   

.. py:data:: DEAD_END
   :annotation: = -

   

.. py:class:: Maze(mazeFileName)

   .. py:method:: drawMaze(self)


   .. py:method:: drawCenteredBox(self, x, y, color)


   .. py:method:: moveTurtle(self, x, y)


   .. py:method:: dropBreadcrumb(self, color)


   .. py:method:: updatePosition(self, row, col, val=None)


   .. py:method:: isExit(self, row, col)


   .. py:method:: __getitem__(self, idx)



.. py:function:: searchFrom(maze, startRow, startColumn)


.. py:data:: myMaze
   

   

