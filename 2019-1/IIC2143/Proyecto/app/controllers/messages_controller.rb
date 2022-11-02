# frozen_string_literal: true

class MessagesController < ApplicationController
  def create
    @message = Message.new(message_params)
    @conversation = Conversation.find(params[:conversation_id])
    @message.user1_id = current_user.id
    @message.user2_id = @conversation.user2_id
    @message.conversation = @conversation
    if @message.save
      redirect_to conversation_messages_path(@conversation)
    else
      redirect_to new_conversation_path
    end
  end

  def index
    @conversation = Conversation.find(params[:conversation_id])
    @usuario2 = User.find_by(id: @conversation.user2_id)
    @usuario1 = User.find_by(id: @conversation.user1_id)
    @message = Message.new
  end

  private

  def message_params
    params.require(:message).permit(:texto)
  end
end
