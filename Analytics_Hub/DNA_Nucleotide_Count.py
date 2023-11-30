import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Function to count nucleotides
def count_nucleotides(sequence):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for nucleotide in sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1
    return counts

# Function to plot bar chart
def plot_bar_chart(counts):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    plt.bar(counts.keys(), counts.values(), color=['red', 'green', 'blue', 'yellow'])
    plt.xlabel('Nucleotide')
    plt.ylabel('Count')
    plt.title('DNA Nucleotide Count')
    st.pyplot()

# Streamlit App
def main():
    st.title('DNA Nucleotide Count App')
    st.write('Enter a DNA sequence to count the occurrences of each nucleotide.')

    # Input text box for DNA sequence
    sequence = st.text_area('Enter DNA Sequence', '')

    if st.button('Count Nucleotides'):
        if sequence:
            # Convert the input to uppercase for consistency
            sequence = sequence.upper()

            # Count nucleotides
            counts = count_nucleotides(sequence)

            # Display the counts
            st.write('**Nucleotide Counts:**')
            st.write(f'A: {counts["A"]}, T: {counts["T"]}, C: {counts["C"]}, G: {counts["G"]}')

            # Plot bar chart
            plot_bar_chart(counts)
        else:
            st.warning('Please enter a DNA sequence.')

if __name__ == '__main__':
    main()
