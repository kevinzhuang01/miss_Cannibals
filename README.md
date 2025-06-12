# Missionaries and Cannibals Solver

This project solves the classic **Missionaries and Cannibals** river crossing puzzle.

## Problem Description

A group of missionaries and cannibals must cross a river using a boat that can carry at most two people. The goal is to move everyone from the left bank to the right bank safely. The challenge is that on either bank, if cannibals outnumber missionaries, the missionaries will be eaten.

## How It Works

The program uses a search-based solution to explore possible safe moves and find a valid sequence of boat crossings that solves the puzzle. It supports different numbers of missionaries and cannibals, and avoids any unsafe situations during the crossing.

## Example Output
DFS ['MC', 'M', 'CC', 'C', 'MM', 'MC', 'MM', 'C', 'CC', 'M', 'MC']

BFS ['CC', 'C', 'CC', 'C', 'MM', 'MC', 'MM', 'C', 'CC', 'M', 'MC']
