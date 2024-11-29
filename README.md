# multibitTrie
AoND-S1-1403-1404-Project#01 implement MultiBit Trie

### Observations:
- Increasing the stride reduces tree depth and improves performance (faster operations and lower memory usage).
- Memory usage is highest at stride 1 and decreases with larger strides.

### Additional Notes:
- The report includes Python code and screenshots of outputs.
- The author uses additional libraries for profiling and performance measurement.

### Results Summary:
1. **Tree Visualization**:
   - Screenshots of the tree structure are provided for strides 1, 2, 4, and 8.

2. **Performance Analysis**:
   - Execution times for each stride:
     - **Stride 1**: ~16.5 seconds
     - **Stride 2**: ~4.6 seconds
     - **Stride 4**: ~2.3 seconds
     - **Stride 8**: ~1.8 seconds
   - As stride increases, tree creation time decreases.

3. **Memory Profiling**:
   - Using `memory-profiler`, memory consumption decreases as stride increases, with stride 1 using the most memory.

4. ### Link Speed Calculation
   - Formula:
     `Link Speed (Gbps) = Total Data Size (bits) / (Transmission Time (seconds) * 10^9)`
   - Results are mentioned briefly in the context of data transmission.
5. **General Observation**:
   - Larger strides reduce the number of trie levels, optimizing both time and memory.
