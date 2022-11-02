# frozen_string_literal: true

class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_many :student_courses, dependent: :destroy
  has_many :professor_courses, dependent: :destroy
  has_many :study_room_comments, dependent: :destroy
  has_many :publicacion_comments, dependent: :destroy
  has_many :study_room_valorations, dependent: :destroy
  has_many :subscribed_user, dependent: :destroy
  has_many :likes, dependent: :destroy
  has_many :like_coments, dependent: :destroy
  has_many :favorite_publications, dependent: :destroy
  has_many :publicacions, dependent: :destroy
  has_many :occupied_rooms, dependent: :destroy
  has_many :study_groups, dependent: :destroy
  has_many :moderated_courses, dependent: :destroy
  has_many :moderation_requests, dependent: :destroy

  has_attached_file :avatar, styles: { medium: '300x300>', thumb: '100x100>' }, default_url: 'profile_pic.jpg'
  validates_attachment_content_type :avatar, content_type: %r{\Aimage/.*\z}
end
