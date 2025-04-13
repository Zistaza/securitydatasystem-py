import streamlit as st
import json
import os

FILENAME = "library.txt"

# Load library
def load_library():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save library
def save_library(library):
    with open(FILENAME, "w") as file:
        json.dump(library, file, indent=4)

# Initialize session state
if "library" not in st.session_state:
    st.session_state.library = load_library()

st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("Menu", [
    "Add a Book", 
    "Remove a Book", 
    "Search Books", 
    "Display All Books", 
    "Statistics"
])

library = st.session_state.library

# Add a Book
if menu == "Add a Book":
    st.header("➕ Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
        genre = st.text_input("Genre")
        read = st.selectbox("Have you read it?", ["No", "Yes"]) == "Yes"
        submitted = st.form_submit_button("Add Book")
        
        if submitted:
            new_book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read": read
            }
            library.append(new_book)
            save_library(library)
            st.success("Book added successfully!")

# Remove a Book
elif menu == "Remove a Book":
    st.header("🗑️ Remove a Book")
    if library:
        titles = [book["title"] for book in library]
        to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            st.session_state.library = [book for book in library if book["title"] != to_remove]
            save_library(st.session_state.library)
            st.success("Book removed successfully!")
    else:
        st.info("Library is empty.")

# Search for a Book
elif menu == "Search Books":
    st.header("🔍 Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    query = st.text_input("Enter search term").lower()
    
    if query:
        if search_by == "Title":
            results = [b for b in library if query in b["title"].lower()]
        else:
            results = [b for b in library if query in b["author"].lower()]
        
        if results:
            st.subheader("Matching Books:")
            for i, book in enumerate(results, 1):
                st.markdown(f"**{i}. {book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found.")

elif menu == "Display All Books":
    st.header("📖 Your Library")
    
    if library:
        # --- Filters ---
        st.subheader("Filters & Sorting")
        genres = list(set(book["genre"] for book in library))
        selected_genre = st.selectbox("Filter by Genre", ["All"] + genres)
        
        read_filter = st.selectbox("Filter by Read Status", ["All", "Read", "Unread"])
        
        sort_by = st.selectbox("Sort by", ["Title", "Author", "Year"])
        sort_order = st.radio("Sort Order", ["Ascending", "Descending"], horizontal=True)

        # --- Apply Filters ---
        filtered_books = library.copy()

        if selected_genre != "All":
            filtered_books = [book for book in filtered_books if book["genre"] == selected_genre]

        if read_filter == "Read":
            filtered_books = [book for book in filtered_books if book["read"]]
        elif read_filter == "Unread":
            filtered_books = [book for book in filtered_books if not book["read"]]

        # --- Sorting ---
        reverse = sort_order == "Descending"
        filtered_books.sort(key=lambda b: str(b[sort_by.lower()]), reverse=reverse)

        # --- Display ---
        if filtered_books:
            for i, book in enumerate(filtered_books, 1):
                st.markdown(
                    f"**{i}. {book['title']}** by {book['author']} ({book['year']}) "
                    f"- *{book['genre']}* - {'✅ Read' if book['read'] else '📖 Unread'}"
                )
        else:
            st.warning("No books match the selected filters.")
    else:
        st.info("Library is empty.")


# Statistics
elif menu == "Statistics":
    st.header("📊 Library Statistics")
    total = len(library)
    read_books = sum(book["read"] for book in library)
    percent = (read_books / total) * 100 if total > 0 else 0
    st.metric("Total Books", total)
    st.metric("Books Read", read_books)
    st.metric("Percentage Read", f"{percent:.1f}%")

st.markdown("""
<div style="background-color:#262730; padding:10px; border-radius:10px; margin-top:30px; text-align:center;">
    <span style="color:white;">🚀 Built by <strong>Zeenat Yameen</strong> | 📚 Personal Library Manager</span>
</div>
""", unsafe_allow_html=True)
