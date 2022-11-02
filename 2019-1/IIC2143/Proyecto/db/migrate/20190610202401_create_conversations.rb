# frozen_string_literal: true

class CreateConversations < ActiveRecord::Migration[5.1]
  def change
    create_table :conversations do |t|
      t.references :user1
      t.references :user2

      t.timestamps
    end
  end
end
