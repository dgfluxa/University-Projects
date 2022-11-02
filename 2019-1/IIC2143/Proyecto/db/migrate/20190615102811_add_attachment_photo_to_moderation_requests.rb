# frozen_string_literal: true

class AddAttachmentPhotoToModerationRequests < ActiveRecord::Migration[5.1]
  def self.up
    change_table :moderation_requests do |t|
      t.attachment :photo
    end
  end

  def self.down
    remove_attachment :moderation_requests, :photo
  end
end
