# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20190615102811) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "buscoclases", force: :cascade do |t|
    t.string "user"
    t.string "course"
    t.integer "time"
    t.integer "id_grupo"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "camps", force: :cascade do |t|
    t.string "nombre"
    t.string "ubicacion"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "url"
  end

  create_table "conversations", force: :cascade do |t|
    t.bigint "user1_id"
    t.bigint "user2_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["user1_id"], name: "index_conversations_on_user1_id"
    t.index ["user2_id"], name: "index_conversations_on_user2_id"
  end

  create_table "courses", force: :cascade do |t|
    t.string "name"
    t.string "sigla"
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "favorite_publications", force: :cascade do |t|
    t.bigint "publicacion_id"
    t.bigint "user_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["publicacion_id"], name: "index_favorite_publications_on_publicacion_id"
    t.index ["user_id"], name: "index_favorite_publications_on_user_id"
  end

  create_table "like_coments", force: :cascade do |t|
    t.bigint "user_id"
    t.bigint "publicacion_comment_id"
    t.integer "like"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["publicacion_comment_id"], name: "index_like_coments_on_publicacion_comment_id"
    t.index ["user_id"], name: "index_like_coments_on_user_id"
  end

  create_table "likes", force: :cascade do |t|
    t.bigint "user_id"
    t.bigint "publicacion_id"
    t.integer "like"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["publicacion_id"], name: "index_likes_on_publicacion_id"
    t.index ["user_id"], name: "index_likes_on_user_id"
  end

  create_table "messages", force: :cascade do |t|
    t.bigint "user1_id"
    t.bigint "user2_id"
    t.bigint "conversation_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.text "texto"
    t.index ["conversation_id"], name: "index_messages_on_conversation_id"
    t.index ["user1_id"], name: "index_messages_on_user1_id"
    t.index ["user2_id"], name: "index_messages_on_user2_id"
  end

  create_table "moderated_courses", force: :cascade do |t|
    t.bigint "user_id"
    t.bigint "course_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["course_id"], name: "index_moderated_courses_on_course_id"
    t.index ["user_id"], name: "index_moderated_courses_on_user_id"
  end

  create_table "moderation_requests", force: :cascade do |t|
    t.bigint "user_id"
    t.bigint "course_id"
    t.text "description"
    t.string "photo"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "photo_file_name"
    t.string "photo_content_type"
    t.integer "photo_file_size"
    t.datetime "photo_updated_at"
    t.index ["course_id"], name: "index_moderation_requests_on_course_id"
    t.index ["user_id"], name: "index_moderation_requests_on_user_id"
  end

  create_table "occupied_rooms", force: :cascade do |t|
    t.bigint "study_room_id"
    t.datetime "from"
    t.datetime "to"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.index ["study_room_id"], name: "index_occupied_rooms_on_study_room_id"
    t.index ["user_id"], name: "index_occupied_rooms_on_user_id"
  end

  create_table "ofertclases", force: :cascade do |t|
    t.integer "precio"
    t.string "course"
    t.string "sala"
    t.text "description"
    t.integer "time"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "user"
  end

  create_table "professor_courses", force: :cascade do |t|
    t.bigint "course_id"
    t.bigint "user_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["course_id"], name: "index_professor_courses_on_course_id"
    t.index ["user_id"], name: "index_professor_courses_on_user_id"
  end

  create_table "publicacion_comments", force: :cascade do |t|
    t.text "body"
    t.bigint "user_id"
    t.bigint "publicacion_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["publicacion_id"], name: "index_publicacion_comments_on_publicacion_id"
    t.index ["user_id"], name: "index_publicacion_comments_on_user_id"
  end

  create_table "publicacions", force: :cascade do |t|
    t.string "titulo"
    t.text "contenido"
    t.text "description"
    t.integer "puntaje"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "course_id"
    t.bigint "user_id"
    t.index ["course_id"], name: "index_publicacions_on_course_id"
    t.index ["user_id"], name: "index_publicacions_on_user_id"
  end

  create_table "student_courses", force: :cascade do |t|
    t.bigint "course_id"
    t.bigint "user_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["course_id"], name: "index_student_courses_on_course_id"
    t.index ["user_id"], name: "index_student_courses_on_user_id"
  end

  create_table "study_groups", force: :cascade do |t|
    t.bigint "course_id"
    t.bigint "study_room_id"
    t.integer "max"
    t.integer "duration"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.index ["course_id"], name: "index_study_groups_on_course_id"
    t.index ["study_room_id"], name: "index_study_groups_on_study_room_id"
    t.index ["user_id"], name: "index_study_groups_on_user_id"
  end

  create_table "study_room_comments", force: :cascade do |t|
    t.bigint "user_id"
    t.text "body"
    t.bigint "study_room_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["study_room_id"], name: "index_study_room_comments_on_study_room_id"
    t.index ["user_id"], name: "index_study_room_comments_on_user_id"
  end

  create_table "study_room_valorations", force: :cascade do |t|
    t.integer "availability"
    t.integer "noise"
    t.integer "plugs"
    t.bigint "user_id"
    t.bigint "study_room_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["study_room_id"], name: "index_study_room_valorations_on_study_room_id"
    t.index ["user_id"], name: "index_study_room_valorations_on_user_id"
  end

  create_table "study_rooms", force: :cascade do |t|
    t.string "name"
    t.string "ubication"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "camp_id"
  end

  create_table "subscribed_users", force: :cascade do |t|
    t.bigint "study_group_id"
    t.bigint "user_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["study_group_id"], name: "index_subscribed_users_on_study_group_id"
    t.index ["user_id"], name: "index_subscribed_users_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "first_name"
    t.string "last_name"
    t.string "avatar_file_name"
    t.string "avatar_content_type"
    t.integer "avatar_file_size"
    t.datetime "avatar_updated_at"
    t.boolean "admin", default: false
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  add_foreign_key "favorite_publications", "publicacions"
  add_foreign_key "favorite_publications", "users"
  add_foreign_key "like_coments", "publicacion_comments"
  add_foreign_key "like_coments", "users"
  add_foreign_key "likes", "publicacions"
  add_foreign_key "likes", "users"
  add_foreign_key "messages", "conversations"
  add_foreign_key "moderated_courses", "courses"
  add_foreign_key "moderated_courses", "users"
  add_foreign_key "moderation_requests", "courses"
  add_foreign_key "moderation_requests", "users"
  add_foreign_key "occupied_rooms", "study_rooms"
  add_foreign_key "occupied_rooms", "users"
  add_foreign_key "professor_courses", "courses"
  add_foreign_key "professor_courses", "users"
  add_foreign_key "publicacion_comments", "publicacions"
  add_foreign_key "publicacion_comments", "users"
  add_foreign_key "publicacions", "users"
  add_foreign_key "student_courses", "courses"
  add_foreign_key "student_courses", "users"
  add_foreign_key "study_groups", "courses"
  add_foreign_key "study_groups", "study_rooms"
  add_foreign_key "study_groups", "users"
  add_foreign_key "study_room_comments", "study_rooms"
  add_foreign_key "study_room_comments", "users"
  add_foreign_key "study_room_valorations", "study_rooms"
  add_foreign_key "study_room_valorations", "users"
  add_foreign_key "subscribed_users", "study_groups"
  add_foreign_key "subscribed_users", "users"
end
