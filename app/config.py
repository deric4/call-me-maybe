from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    account_sid: str = Field(..., env='TWILIO_ACCOUNT_SID')
    auth_token: str = Field(..., env='TWILIO_AUTH_TOKEN')
    
    conference_phone: str = Field(..., env='CONFERENCE_PHONE') 
    agent_phone: str =  Field(..., env='AGENT_PHONE') 
    personal_phone: str = Field(..., env='PERSONAL_PHONE')
    office_phone: str = Field(..., env='OFFICE_PHONE')

    class Config:
        env_file = '.env'


settings = Settings()
