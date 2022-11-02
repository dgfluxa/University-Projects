# frozen_string_literal: true

class ConversationsController < ApplicationController
  def create
    @us2 = User.find(params[:id])
    @us1 = current_user
    conversation1 = Conversation.find_by(user1_id: @us2.id, user2_id: @us1.id)
    conversation2 = Conversation.find_by(user1_id: @us1.id, user2_id: @us2.id)
    if conversation1.nil? && conversation2.nil?
      @conversation = Conversation.new
      @conversation.user1_id = @us1.id
      @conversation.user2_id = @us2.id
      if @conversation.save
        redirect_to conversation_messages_path(@conversation)
      else
        redirect_to new_conversation_path
      end
    else
      if !conversation1.nil?
        redirect_to conversation_messages_path(conversation1)
      else
        redirect_to conversation_messages_path(conversation2)
      end
    end
  end

  def show
    @conversation = Conversation.find(params[:id])
    @usuario2 = User.find_by(id: @conversation.user2_id)
    @message = Message.new
  end
end
