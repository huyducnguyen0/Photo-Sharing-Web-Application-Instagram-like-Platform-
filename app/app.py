from fastapi import FastAPI, HTTPException 
from app.schemas import PostCreate
from app.db import Post, create_db_and_tables, get_async_session_maker

from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    await create_db_and_tables()
    yield 


app = FastAPI(lifespan=lifespan) 

text_posts = {
    1: {"title": "Morning Coding", "content": "Started my day with some Python and coffee ☕. Feeling productive!", "author": "ducdev"},
    2: {"title": "FastAPI Tips", "content": "Just learned how to build APIs with FastAPI. Super fast and clean!", "author": "backendguy"},
    3: {"title": "Gym + Code", "content": "Morning gym session done 💪 Now back to coding!", "author": "fitcoder"},
    4: {"title": "Bug Hunting", "content": "Spent 2 hours fixing a bug... turns out it was just a typo 🤡", "author": "debuglife"},
    5: {"title": "AI Agent", "content": "Experimenting with AI agents and automation. This is the future.", "author": "ai_builder"},
    6: {"title": "Late Night Code", "content": "Coding at 2AM hits different. Silence + focus.", "author": "nightowl"},
    7: {"title": "Frontend Struggle", "content": "CSS is harder than backend sometimes 😭", "author": "fullstacknoob"},
    8: {"title": "Hackathon Prep", "content": "Preparing ideas for upcoming hackathon. Thinking about AI + Web.", "author": "hustler"},
    9: {"title": "Database Design", "content": "Designing database schemas is actually fun when you get it.", "author": "datageek"},
    10: {"title": "First API", "content": "Finally deployed my first API. Feels amazing!", "author": "newbie"},
    11: {"title": "Learning Curve", "content": "Every day learning something new. Today: async/await in Python.", "author": "learner"},
    12: {"title": "Coffee Break", "content": "Sometimes you just need a break and a good cup of coffee.", "author": "chilldev"},
    13: {"title": "Startup Dream", "content": "One day I’ll build a product used by millions 🚀", "author": "dreamer"},
    14: {"title": "Clean Code", "content": "Refactored my code today. Looks 10x cleaner now.", "author": "perfectionist"},
    15: {"title": "Error 500", "content": "Server crashed again... time to check logs 🔥", "author": "backendpain"},
    16: {"title": "AI + Web", "content": "Combining AI with web apps is insanely powerful.", "author": "innovator"},
    17: {"title": "Consistency", "content": "Small progress every day > big progress once in a while.", "author": "discipline"},
    18: {"title": "Debug Mode", "content": "print() is still the best debugger 😆", "author": "oldschool"},
    19: {"title": "Deploy Day", "content": "Deployed my project today. Fingers crossed 🤞", "author": "builder"},
    20: {"title": "Keep Going", "content": "No matter how hard it gets, just keep coding.", "author": "grinder"}
}
@app.get("/posts")
def get_all_post(limit: int  ):
    if limit: 
        return list(text_posts.values())[:limit]      
    return text_posts
     
@app.get("/posts/{id}")
def get_post(id : int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")

    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title" : post.title, "content": post.content}
    
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post
